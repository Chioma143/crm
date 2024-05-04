import functools

from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db
from flaskr.auth import login_required

blueprint = Blueprint('sale', __name__, url_prefix='/sale')

@blueprint.route('/', methods=('GET', 'POST'))
@login_required
def index():
  db = get_db()
  error = None
  # Get business ID
  businessid = g.user['BusinessID']

  if request.method == 'POST':
    customerid = request.form['customerid']
    productid = request.form['productid']
    quantity = request.form['quantity']
    saledate = request.form['saledate']

    if not customerid or not productid or not quantity or not saledate:
      error = 'All fields are required.'
    else:
      try:
        # Get product price
        product = db.execute(
          "SELECT Price FROM Product WHERE ProductID = ? AND BusinessID = ?",
          (productid, businessid)
        ).fetchone()

        if product:
          price_per_unit = product['Price']
          total_price = int(quantity) * price_per_unit

          db.execute(
            "INSERT INTO Sales (CustomerID, ProductID, Quantity, TotalPrice, SaleDate, BusinessID) VALUES (?, ?, ?, ?, ?, ?)",
            (customerid, productid, quantity, total_price, saledate, businessid)
          )
          db.commit()
          flash('Sale created successfully', 'success')
        else:
          flash('Product not found or does not belong to your business', 'error')
      except db.Error as e:
        error = str(e)
        flash('An error occurred while creating the sale: {}'.format(error), 'error')

  customers = db.execute(
    "SELECT * FROM Customer WHERE BusinessID = ?", (businessid,)
  ).fetchall()

  products = db.execute(
    "SELECT * FROM Product WHERE BusinessID = ?", (businessid,)
  ).fetchall()

  # Add pagination to sales lists
  page = request.args.get('page', 1, type=int)
  per_page = 15
  offset = (page - 1) * per_page

  sales = db.execute(
    "SELECT s.*, p.*, c.CustomerName FROM Sales s JOIN Product p ON s.ProductID = p.ProductID JOIN Customer c ON s.CustomerID = c.CustomerID WHERE s.BusinessID = ? LIMIT ? OFFSET ?",
    (businessid, per_page, offset,)
  ).fetchall()

  # Convert Row objects to dictionaries
  sales = [dict(row) for row in sales]

  # Determine if there are more pages
  has_prev = page > 1
  has_next = len(sales) == per_page

  return render_template('sale/index.html', sales=sales, customers=customers, products=products, has_prev=has_prev, has_next=has_next, page=page)

# @blueprint.route('/update', methods=('POST',))
# @login_required
# def update():
#   db = get_db()
#   error = None

#   if request.method == 'POST':
#     try:
#       customerid = request.form['customerid']
#       name = request.form['name']
#       email = request.form['email']
#       phone = request.form['phone']
#       industry = request.form['industry']
#       location = request.form['location']

#       # Get business ID
#       businessid = g.user['BusinessID']

#       if not customerid or not name or not email or not phone or not industry or not location:
#         error = 'All fields are required.'
#       else:
#         db.execute(
#           "UPDATE Customer SET CustomerName = ?, Email = ?, Phone = ?, Industry = ?, Location = ? WHERE CustomerID = ? AND BusinessID = ?",
#           (name, email, phone, industry, location, customerid, businessid)
#         )
#         db.commit()
#         flash('Customer updated successfully', 'success')
#     except db.Error as e:
#       error = str(e)
#       flash('An error occurred while updating the customer: {}'.format(error), 'error')

#   if error:
#     flash(error, 'error')

#   return redirect(url_for('customer.index'))

@blueprint.route('/<sale_id>/delete')
@login_required
def delete(sale_id):
  db = get_db()
  error = None
  # Get business ID
  businessid = g.user['BusinessID']

  try:
    db.execute("DELETE FROM Sales WHERE SaleID = ? AND BusinessID = ?", (sale_id, businessid))
    db.commit()
    flash('Sale deleted successfully', 'success')
  except db.Error as e:
    error = str(e)
    flash('An error occurred while deleting the sale: {}'.format(error), 'error')

  return redirect(url_for('sale.index'))