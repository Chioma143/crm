import os

from flask import (Flask, render_template)
from flaskr.auth import login_required
from flaskr.db import get_db
from . import (db, auth, customer, group)

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='CRM-DEV100',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    db.init_app(app)
    app.register_blueprint(auth.blueprint)
    app.register_blueprint(customer.blueprint)
    app.register_blueprint(group.blueprint)

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
        total_industries = db.execute(
            "SELECT COUNT(DISTINCT Industry) AS TotalIndustries FROM Company"
        ).fetchone()[0]
        total_customers = db.execute(
            "SELECT COUNT(*) FROM Company"
        ).fetchone()[0]
        total_users = db.execute(
            "SELECT COUNT(*) FROM User"
        ).fetchone()[0]
        chart = db.execute(
            "SELECT Industry, COUNT(*) AS Total FROM Company GROUP BY Industry;"
        ).fetchall()
        return render_template('dashboard.html', total_industries=total_industries, total_customers=total_customers, total_users=total_users, chart=chart)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
