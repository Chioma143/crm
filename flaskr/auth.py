import functools
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db

blueprint = Blueprint('auth', __name__, url_prefix='/auth')

@blueprint.route('/register', methods=('GET', 'POST'))
def register():
  if request.method == 'POST':
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    businessname = request.form['businessname']
    db = get_db()
    error = None

    if not username:
      error = 'Username is required.'
    elif not email:
      error = 'Email is required'
    elif not password:
      error = 'Password is required'
    elif not firstname:
      error = 'First name is required'
    elif not lastname:
      error = 'Last name is required'
    elif not businessname:
      error = 'Business name is required'

    usertype = 'admin'
    
    if error is None:
      try:
        # Create user
        db.execute(
          "INSERT INTO User (Username, Email, Password, FirstName, LastName, UserType) VALUES (?, ?, ?, ?, ?, ?)",
          (username, email, generate_password_hash(password), firstname, lastname, usertype)
        )
        db.commit()

        # Create business
        db.execute(
          "INSERT INTO Business (BusinessName) VALUES (?)",
          (businessname,)
        )
        db.commit()

        # Retrieve newly created business ID
        business_cur = db.execute(
          "SELECT BusinessID FROM Business WHERE BusinessName = ?",
          (businessname,)
        )
        business = business_cur.fetchone()

        # Update user with BusinessID
        db.execute(
          "UPDATE User SET BusinessID = ? WHERE Username = ?",
          (business['BusinessID'], username)
        )
        db.commit()

        # Create CRM
        db.execute(
          "INSERT INTO CRM (CRMName, BusinessID) VALUES (?, ?)",
          ('Default CRM', business['BusinessID'])
        )
        db.commit()
      except db.IntegrityError:
        error = f"User {username} is already registered."
      else:
        return redirect(url_for("auth.login"))
      
    flash(error)
  return render_template('auth/register.html')

@blueprint.route('/login', methods=('GET', 'POST'))
def login():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']

    db = get_db()
    error = None
    user = db.execute(
      "SELECT * FROM User WHERE Username = ?", (username,)
    ).fetchone()

    if user is None:
      error = "Incorrect username."
    elif not check_password_hash(user['password'], password):
      error = "Incorrect password."
    
    if error is None:
      session.clear()
      session['user_id'] = user['UserID']
      return redirect(url_for('index'))
    
    flash(error)
  return render_template('auth/login.html')

@blueprint.before_app_request
def load_logged_in_user():
  user_id = session.get('user_id')

  if user_id is None:
    g.user = None
  else:
    g.user = get_db().execute(
      "SELECT u.*, b.* FROM User u LEFT JOIN Business b ON u.BusinessID = b.BusinessID WHERE u.UserID = ?", (user_id,)
    ).fetchone()

def login_required(view):
  @functools.wraps(view)
  def wrapped_view(**kwargs):
    if g.user is None:
      return redirect(url_for('auth.login'))
    return view(**kwargs)
  return wrapped_view

@blueprint.route('/logout')
def logout():
  session.clear()
  return redirect(url_for('index'))