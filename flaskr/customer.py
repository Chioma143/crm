import functools

from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db
from flaskr.auth import login_required

blueprint = Blueprint('customer', __name__, url_prefix='/customer')

@blueprint.route('/', methods=('GET', 'POST'))
@login_required
def index():
  db = get_db()
  error = None
  # Get business ID
  businessid = g.user['BusinessID']

  if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    industry = request.form['industry']
    location = request.form['location']

    if not name or not email or not phone or not industry or not location:
      error = 'All fields are required.'
    else:
      try:
        db.execute(
          "INSERT INTO Customer (CustomerName, Email, Phone, Industry, Location, BusinessID) VALUES (?, ?, ?, ?, ?, ?)",
          (name, email, phone, industry, location, businessid)
        )
        db.commit()
        flash('Customer created successfully', 'success')
      except db.Error as e:
        error = str(e)
        flash('An error occurred while creating the customer: {}'.format(error), 'error')

  # Add pagination to customer lists
  page = request.args.get('page', 1, type=int)
  per_page = 15
  offset = (page - 1) * per_page

  customers = db.execute(
    "SELECT * FROM Customer WHERE BusinessID = ? LIMIT ? OFFSET ?",
    (businessid, per_page, offset)
  ).fetchall()

  # Convert Row objects to dictionaries
  customers = [dict(row) for row in customers]

  # Determine if there are more pages
  has_prev = page > 1
  has_next = len(customers) == per_page

  return render_template('customer/index.html', customers=customers, has_prev=has_prev, has_next=has_next, page=page)

@blueprint.route('/update', methods=('POST',))
@login_required
def update():
  db = get_db()
  error = None

  if request.method == 'POST':
    try:
      customerid = request.form['customerid']
      name = request.form['name']
      email = request.form['email']
      phone = request.form['phone']
      industry = request.form['industry']
      location = request.form['location']

      # Get business ID
      businessid = g.user['BusinessID']

      if not customerid or not name or not email or not phone or not industry or not location:
        error = 'All fields are required.'
      else:
        db.execute(
          "UPDATE Customer SET CustomerName = ?, Email = ?, Phone = ?, Industry = ?, Location = ? WHERE CustomerID = ? AND BusinessID = ?",
          (name, email, phone, industry, location, customerid, businessid)
        )
        db.commit()
        flash('Customer updated successfully', 'success')
    except db.Error as e:
      error = str(e)
      flash('An error occurred while updating the customer: {}'.format(error), 'error')

  if error:
    flash(error, 'error')

  return redirect(url_for('customer.index'))

@blueprint.route('/<customer_id>/delete')
@login_required
def delete(customer_id):
  db = get_db()
  error = None
  # Get business ID
  businessid = g.user['BusinessID']

  try:
    db.execute("DELETE FROM Customer WHERE CustomerID = ? AND BusinessID = ?", (businessid, customer_id,))
    db.commit()
    flash('Customer deleted successfully', 'success')
  except db.Error as e:
    error = str(e)
    flash('An error occurred while deleting the customer: {}'.format(error), 'error')

  return redirect(url_for('customer.index'))