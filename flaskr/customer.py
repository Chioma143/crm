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

  if request.method == 'POST':
    name = request.form['name']
    industry = request.form['industry']
    location = request.form['location']
    customer = request.form['customer']

    if not name or not industry or not location or not customer:
      error = 'All fields are required.'
    else:
      try:
        db.execute(
          "INSERT INTO Company (CompanyName, Industry, Location, UserID) VALUES (?, ?, ?, ?)",
          (name, industry, location, customer)
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
    "SELECT * FROM Company LIMIT ? OFFSET ?",
    (per_page, offset)
  ).fetchall()

  # Determine if there are more pages
  has_prev = page > 1
  has_next = len(customers) == per_page

  users = db.execute(
    "SELECT UserID, Email FROM User"
  ).fetchall()
  return render_template('customer/index.html', customers=customers, users=users, has_prev=has_prev, has_next=has_next, page=page)

@blueprint.route('/<customer_id>/delete')
@login_required
def delete(customer_id):
  db = get_db()
  error = None

  try:
    db.execute("DELETE FROM Company WHERE CompanyID = ?", (customer_id,))
    db.commit()
    flash('Customer deleted successfully', 'success')
  except db.Error as e:
    error = str(e)
    flash('An error occurred while deleting the customer: {}'.format(error), 'error')

  return redirect(url_for('customer.index'))