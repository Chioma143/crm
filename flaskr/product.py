import functools

from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db
from flaskr.auth import login_required

blueprint = Blueprint('product', __name__, url_prefix='/product')

@blueprint.route('/', methods=('GET', 'POST'))
@login_required
def index():
  db = get_db()
  error = None
  # Get business ID
  businessid = g.user['BusinessID']
  

  if request.method == 'POST':
    name = request.form['name']
    description = request.form['description']
    price = request.form['price']
    currency = request.form['currency']
    category = request.form['category']

    if not name or not description or not price or not currency or not category:
      error = 'All fields are required.'
    else:
      try:
        db.execute(
          "INSERT INTO Product (ProductName, Description, Price, Currency, Category, BusinessID) VALUES (?, ?, ?, ?, ?, ?)",
          (name, description, price, currency, category, businessid)
        )
        db.commit()
        flash('Product created successfully', 'success')
      except db.Error as e:
        error = str(e)
        flash('An error occurred while creating the product: {}'.format(error), 'error')

  # Add pagination to customer lists
  page = request.args.get('page', 1, type=int)
  per_page = 15
  offset = (page - 1) * per_page

  products = db.execute(
    "SELECT * FROM Product WHERE BusinessID = ? LIMIT ? OFFSET ?",
    (businessid, per_page, offset)
  ).fetchall()

  # Convert Row objects to dictionaries
  products = [dict(row) for row in products]

  # Determine if there are more pages
  has_prev = page > 1
  has_next = len(products) == per_page

  return render_template('product/index.html', products=products, has_prev=has_prev, has_next=has_next, page=page)

@blueprint.route('/update', methods=('POST',))
@login_required
def update():
  db = get_db()
  error = None
  # Get business ID
  businessid = g.user['BusinessID']

  if request.method == 'POST':
    try:
      productid = request.form['productid']
      name = request.form['name']
      description = request.form['description']
      price = request.form['price']
      currency = request.form['currency']
      category = request.form['category']

      if not name or not description or not price or not currency or not category:
        error = 'All fields are required.'
      else:
        db.execute(
          "UPDATE Product SET ProductName = ?, Description = ?, Price = ?, Currency = ?, Category = ? WHERE ProductID = ? AND BusinessID = ?",
          (name, description, price, currency, category, productid, businessid)
        )
        db.commit()
        flash('Product updated successfully', 'success')
    except db.Error as e:
      error = str(e)
      flash('An error occurred while updating the product: {}'.format(error), 'error')

  if error:
    flash(error, 'error')

  return redirect(url_for('product.index'))

@blueprint.route('/<product_id>/delete')
@login_required
def delete(product_id):
  db = get_db()
  error = None
  # Get business ID
  businessid = g.user['BusinessID']

  try:
    db.execute("DELETE FROM Product WHERE ProductID = ? AND BusinessID = ?", (product_id, businessid,))
    db.commit()
    flash('Product deleted successfully', 'success')
  except db.Error as e:
    error = str(e)
    flash('An error occurred while deleting the customer: {}'.format(error), 'error')

  return redirect(url_for('product.index'))