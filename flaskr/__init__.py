import os

from flask import (Flask, render_template, g, request)
from flaskr.auth import login_required
from flaskr.db import get_db
from . import (db, auth, customer, group, product, setting, analytic, sale, search, setup)

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='CRM-DEV100',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    db.init_app(app)
    app.register_blueprint(setup.blueprint)
    app.register_blueprint(auth.blueprint)
    app.register_blueprint(customer.blueprint)
    app.register_blueprint(group.blueprint)
    app.register_blueprint(product.blueprint)
    app.register_blueprint(setting.blueprint)
    app.register_blueprint(analytic.blueprint)
    app.register_blueprint(sale.blueprint)
    app.register_blueprint(search.blueprint)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # routes
    @app.route('/')
    @login_required
    def index():
        db = get_db()
        # Get business ID
        businessid = g.user['BusinessID']
        total_customers = db.execute("SELECT COUNT(*) FROM Customer WHERE BusinessID = ?", (businessid,)).fetchone()[0]
        total_users = db.execute("SELECT COUNT(*) FROM User WHERE BusinessID = ?", (businessid,)).fetchone()[0]
        total_sales = db.execute("SELECT SUM(s.Quantity * p.Price) AS TotalSales FROM Sales s JOIN Product p ON s.ProductID = p.ProductID WHERE s.BusinessID = ?", (businessid,)).fetchone()[0]
        # Retrieve chart data for products by category
        chart = db.execute(
            "SELECT Category, COUNT(*) AS Total FROM Product WHERE BusinessID = ? GROUP BY Category", 
            (businessid,)
        ).fetchall()

        total_sales_quantities = db.execute("SELECT COUNT(s.Quantity) AS TotalQuantity FROM Sales s WHERE s.BusinessID = ?", (businessid,)).fetchone()[0]

        sales = db.execute(
            "SELECT s.*, p.*, c.CustomerName FROM Sales s JOIN Product p ON s.ProductID = p.ProductID JOIN Customer c ON s.CustomerID = c.CustomerID WHERE s.BusinessID = ? ORDER BY SaleDate DESC LIMIT 10",
            (businessid,)
        ).fetchall()

        # Convert Row objects to dictionaries
        sales = [dict(row) for row in sales]

        if total_sales is not None:
            total_sales = "£{:,.2f}".format(total_sales)
        else:
            total_sales = "0.00"

        return render_template('dashboard.html', total_customers=total_customers, total_users=total_users, total_sales=total_sales, sales=sales, total_sales_quantities=total_sales_quantities, chart=chart)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
