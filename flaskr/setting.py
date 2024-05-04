import functools

from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db
from flaskr.auth import login_required

blueprint = Blueprint('setting', __name__, url_prefix='/setting')

@blueprint.route('/', methods=('GET', 'POST'))
@login_required
def index():
  db = get_db()
  error = None
  # Get business ID
  businessid = g.user['BusinessID']

  if request.method == 'POST':
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    usertype = request.form['usertype']

    if not firstname or not lastname or not email or not username or not password or not usertype:
      error = 'All fields are required.'
    else:
      try:
        # Create user
        db.execute(
          "INSERT INTO User (Username, Email, Password, FirstName, LastName, UserType, BusinessID) VALUES (?, ?, ?, ?, ?, ?, ?)",
          (username, email, generate_password_hash(password), firstname, lastname, usertype, businessid)
        )
        db.commit()
        flash('User created successfully', 'success')
      except db.Error as e:
        error = str(e)
        flash('An error occurred while creating the user: {}'.format(error), 'error')

  # Add pagination to customer lists
  page = request.args.get('page', 1, type=int)
  per_page = 15
  offset = (page - 1) * per_page

  users = db.execute(
    "SELECT * FROM User WHERE BusinessID = ? LIMIT ? OFFSET ?",
    (businessid, per_page, offset)
  ).fetchall()

  # Convert Row objects to dictionaries
  users = [dict(row) for row in users]

  # Determine if there are more pages
  has_prev = page > 1
  has_next = len(users) == per_page

  return render_template('setting/index.html', users=users, has_prev=has_prev, has_next=has_next, page=page)

@blueprint.route('/user')
@login_required
def user():
  db = get_db()
  # Get User ID
  userid = g.user['UserID']
  # Get business ID
  businessid = g.user['BusinessID']

  user = db.execute(
    "SELECT * FROM User WHERE UserID = ? AND BusinessID = ?",
    (userid, businessid,)
  ).fetchone()

  return render_template('setting/user.html', user=user)

@blueprint.route('/update', methods=('POST',))
@login_required
def update():
  db = get_db()
  error = None

  if request.method == 'POST':
    try:
      userid = request.form['userid']
      firstname = request.form['firstname']
      lastname = request.form['lastname']
      email = request.form['email']
      username = request.form['username']
      password = request.form['password']
      usertype = request.form['usertype']

      # Get business ID
      businessid = g.user['BusinessID']

      if not firstname or not lastname or not email or not username or not usertype:
        error = 'All fields are required.'
      else:
        # Check if password is provided
        if password:
          db.execute(
              "UPDATE User SET FirstName = ?, LastName = ?, Email = ?, Username = ?, Password = ?, UserType = ? WHERE UserID = ? AND BusinessID = ?",
              (firstname, lastname, email, username, generate_password_hash(password), usertype, userid, businessid)
          )
        else:
          db.execute(
              "UPDATE User SET FirstName = ?, LastName = ?, Email = ?, Username = ?, UserType = ? WHERE UserID = ? AND BusinessID = ?",
              (firstname, lastname, email, username, usertype, userid, businessid)
          )
        db.commit()
        flash('User updated successfully', 'success')
    except db.Error as e:
      error = str(e)
      flash('An error occurred while updating the user: {}'.format(error), 'error')

  if error:
    flash(error, 'error')

  return redirect(url_for('setting.index'))

@blueprint.route('/<user_id>/delete')
@login_required
def delete(user_id):
  db = get_db()
  error = None
  # Get business ID
  businessid = g.user['BusinessID']

  try:
    db.execute("DELETE FROM User WHERE UserID = ? AND BusinessID = ?", (user_id, businessid,))
    db.commit()
    flash('User deleted successfully', 'success')
  except db.Error as e:
    error = str(e)
    flash('An error occurred while deleting the user: {}'.format(error), 'error')

  return redirect(url_for('setting.index'))