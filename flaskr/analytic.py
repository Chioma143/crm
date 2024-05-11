import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from flaskr.db import get_db
from flaskr.auth import login_required

blueprint = Blueprint('analytic', __name__, url_prefix='/analytic')

@blueprint.route('/', methods=('GET', 'POST'))
@login_required
def index():
  db = get_db()
  # Get business ID
  businessid = g.user['BusinessID']

  # Fetch analytics data from the database
  total_sales = db.execute("SELECT SUM(s.Quantity * p.Price) AS TotalSales FROM Sales s JOIN Product p ON s.ProductID = p.ProductID WHERE s.BusinessID = ?;", (businessid,)).fetchone()[0]
  total_customers = db.execute("SELECT COUNT(*) FROM Customer WHERE BusinessID = ?", (businessid,)).fetchone()[0]
  total_products = db.execute("SELECT COUNT(*) FROM Product WHERE BusinessID = ?", (businessid,)).fetchone()[0]
  total_businesses = db.execute("SELECT COUNT(*) FROM Business").fetchone()[0]
  total_crms = db.execute("SELECT COUNT(*) FROM CRM WHERE BusinessID = ?", (businessid,)).fetchone()[0]
  total_sales_quantities = db.execute("SELECT COUNT(s.Quantity) AS TotalQuantity FROM Sales s WHERE s.BusinessID = ?", (businessid,)).fetchone()[0]

  # Fetch product analytics by category and price
  product_categories = db.execute("""
      SELECT Category, COUNT(*) AS TotalProducts, AVG(Price) AS AvgPrice
      FROM Product
      WHERE BusinessID = ?
      GROUP BY Category
      ORDER BY TotalProducts DESC
      LIMIT 5
  """, (businessid,)).fetchall()

  # Fetch sales analytics by quantity
  sales_by_quantity = db.execute("""
      SELECT ProductID, SUM(Quantity) AS TotalQuantity
      FROM Sales
      WHERE BusinessID = ?
      GROUP BY ProductID
      ORDER BY TotalQuantity DESC
      LIMIT 5
  """, (businessid,)).fetchall()

  # Format data for charts
  chart_data = {
      'sales_labels': ['Total Sales'],
      'total_sales': [total_sales],
      'customer_labels': ['Total Customers'],
      'total_customers': [total_customers],
      'product_labels': ['Total Products Sold'],
      'total_products': [total_products],
      'business_labels': ['Total Businesses Registered'],
      'total_businesses': [total_businesses],
      'crm_labels': ['Total CRMs'],
      'total_crms': [total_crms],
      'product_category_labels': [row['Category'] for row in product_categories],
      'product_category_data': [row['TotalProducts'] for row in product_categories],
      'product_avg_price_data': [row['AvgPrice'] for row in product_categories],
      'sales_quantity_labels': [row['ProductID'] for row in sales_by_quantity],
      'sales_quantity_data': [row['TotalQuantity'] for row in sales_by_quantity]
  }

  return render_template('analytic/index.html', chart_data=chart_data, total_sales_quantities=total_sales_quantities)
