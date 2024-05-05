from flask import (Blueprint, render_template, flash, g, jsonify, request)
from flaskr.db import get_db
from flaskr.auth import login_required

blueprint = Blueprint('search', __name__, url_prefix='/search')

@blueprint.route('/')
@login_required
def index():
  db = get_db()
  error = None
  # Get business ID
  businessid = g.user['BusinessID']

  # Get search query from request parameters
  search_query = request.args.get('query', '')

  try:
    # Search customers
    customers = db.execute(
      "SELECT * FROM Customer WHERE BusinessID = ? AND CustomerName LIKE ?",
      (businessid, f'%{search_query}%')
    ).fetchall()

    # Search products
    products = db.execute(
      "SELECT * FROM Product WHERE BusinessID = ? AND (ProductName LIKE ? OR Category LIKE ?)",
      (businessid, f'%{search_query}%', f'%{search_query}%')
    ).fetchall()

    # Search sales
    sales = db.execute(
      "SELECT * FROM Sales WHERE BusinessID = ? AND SaleDate LIKE ?",
      (businessid, f'%{search_query}%')
    ).fetchall()

    # Convert Row objects to dictionaries
    customers = [dict(row) for row in customers]
    products = [dict(row) for row in products]
    sales = [dict(row) for row in sales]

    # Return search results as JSON
    return render_template('search.html', customers=customers, products=products, sales=sales)
  except db.Error as e:
    error = str(e)
    flash('An error occurred during search: {}'.format(error), 'error')
    return jsonify(error=error), 500
