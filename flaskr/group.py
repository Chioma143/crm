import functools

from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db
from flaskr.auth import login_required

blueprint = Blueprint('group', __name__, url_prefix='/group')

@blueprint.route('/', methods=('GET', 'POST'))
@login_required
def index():
  db = get_db()
  error = None
  # Get business ID
  businessid = g.user['BusinessID']

  # Add pagination to customer lists
  page = request.args.get('page', 1, type=int)
  per_page = 15
  offset = (page - 1) * per_page

  groups = db.execute(
    "SELECT * FROM Customer WHERE BusinessID = ? ORDER BY Industry LIMIT ? OFFSET ?",
    (businessid, per_page, offset)
  ).fetchall()

  # Convert Row objects to dictionaries
  groups = [dict(row) for row in groups]

  # Determine if there are more pages
  has_prev = page > 1
  has_next = len(groups) == per_page

  return render_template('group.html', groups=groups, has_prev=has_prev, has_next=has_next, page=page)