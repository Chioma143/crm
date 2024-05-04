from flask import (Blueprint, flash, g, redirect, url_for)
from flaskr.db import get_db
from flaskr.auth import login_required

blueprint = Blueprint('setup', __name__, url_prefix='/setup')

@blueprint.route('/import')
@login_required
def index():
  db = get_db()
  error = None
  # Get business ID
  businessid = g.user['BusinessID']

  # Insert data into the database
  try:
    script = '''
      -- Insert Customer data
      INSERT INTO Customer (CustomerName, Email, Phone, Industry, Location, BusinessID)
      VALUES 
          ('John Smith', 'john.smith@example.com', '+1234567891', 'Technology', 'London', ?),
          ('Mary Johnson', 'mary.johnson@example.com', '+1234567892', 'Retail', 'Manchester', ?),
          ('Michael Williams', 'michael.williams@example.com', '+1234567893', 'Fashion', 'Birmingham', ?),
          ('Jennifer Brown', 'jennifer.brown@example.com', '+1234567894', 'Technology', 'Leeds', ?),
          ('Christopher Jones', 'christopher.jones@example.com', '+1234567895', 'Retail', 'Glasgow', ?),
          ('Amanda Davis', 'amanda.davis@example.com', '+1234567896', 'Fashion', 'Liverpool', ?),
          ('James Miller', 'james.miller@example.com', '+1234567897', 'Technology', 'Bristol', ?),
          ('Jessica Wilson', 'jessica.wilson@example.com', '+1234567898', 'Retail', 'Edinburgh', ?),
          ('David Martinez', 'david.martinez@example.com', '+1234567899', 'Fashion', 'Sheffield', ?),
          ('Linda Taylor', 'linda.taylor@example.com', '+1234567800', 'Technology', 'Newcastle', ?),
          ('Matthew Anderson', 'matthew.anderson@example.com', '+1234567801', 'Retail', 'Cardiff', ?),
          ('Barbara Thomas', 'barbara.thomas@example.com', '+1234567802', 'Fashion', 'Belfast', ?),
          ('Richard Jackson', 'richard.jackson@example.com', '+1234567803', 'Technology', 'Dublin', ?),
          ('Sarah White', 'sarah.white@example.com', '+1234567804', 'Retail', 'Aberdeen', ?),
          ('Daniel Harris', 'daniel.harris@example.com', '+1234567805', 'Fashion', 'Cambridge', ?),
          ('Nancy Clark', 'nancy.clark@example.com', '+1234567806', 'Technology', 'Oxford', ?),
          ('Karen Lewis', 'karen.lewis@example.com', '+1234567807', 'Retail', 'York', ?),
          ('Mark King', 'mark.king@example.com', '+1234567808', 'Fashion', 'Brighton', ?),
          ('Lisa Scott', 'lisa.scott@example.com', '+1234567809', 'Technology', 'Nottingham', ?),
          ('Paul Green', 'paul.green@example.com', '+1234567810', 'Retail', 'Southampton', ?);

      -- Insert Product data
      INSERT INTO Product (ProductName, Description, Price, Currency, Category, BusinessID)
      VALUES 
          ('Laptop', 'High-performance laptop with SSD storage', 999.99, 'GBP', 'Electronics', ?),
          ('Smartphone', 'Latest smartphone with advanced camera features', 799.99, 'GBP', 'Electronics', ?),
          ('Wireless Headphones', 'Premium wireless headphones with noise cancellation', 199.99, 'GBP', 'Electronics', ?),
          ('Coffee Machine', 'Espresso machine with built-in grinder', 299.99, 'GBP', 'Kitchen Appliances', ?),
          ('Smart TV', '4K smart TV with HDR support', 899.99, 'GBP', 'Electronics', ?),
          ('Fitness Tracker', 'Waterproof fitness tracker with heart rate monitoring', 129.99, 'GBP', 'Health & Fitness', ?),
          ('Gaming Console', 'Next-gen gaming console with 4K gaming support', 449.99, 'GBP', 'Electronics', ?),
          ('Wireless Router', 'High-speed wireless router with extended range', 79.99, 'GBP', 'Electronics', ?),
          ('Portable Speaker', 'Bluetooth portable speaker with long battery life', 69.99, 'GBP', 'Electronics', ?),
          ('Robot Vacuum Cleaner', 'Smart robot vacuum cleaner with mapping technology', 349.99, 'GBP', 'Home Appliances', ?),
          ('Digital Camera', 'Professional digital camera with interchangeable lenses', 1199.99, 'GBP', 'Electronics', ?),
          ('Electric Toothbrush', 'Electric toothbrush with multiple cleaning modes', 49.99, 'GBP', 'Health & Beauty', ?),
          ('Wireless Mouse', 'Ergonomic wireless mouse for comfortable use', 29.99, 'GBP', 'Electronics', ?),
          ('Blender', 'High-powered blender for making smoothies and shakes', 89.99, 'GBP', 'Kitchen Appliances', ?),
          ('External Hard Drive', 'Portable external hard drive for data backup', 129.99, 'GBP', 'Electronics', ?),
          ('Fitness Watch', 'Smart fitness watch with GPS tracking', 199.99, 'GBP', 'Health & Fitness', ?),
          ('Hair Dryer', 'Professional hair dryer with ion technology', 79.99, 'GBP', 'Health & Beauty', ?),
          ('Air Purifier', 'HEPA air purifier for cleaner indoor air', 149.99, 'GBP', 'Home Appliances', ?),
          ('Electric Kettle', 'Fast-boiling electric kettle for tea and coffee', 39.99, 'GBP', 'Kitchen Appliances', ?),
          ('Wireless Earbuds', 'True wireless earbuds with noise isolation', 149.99, 'GBP', 'Electronics', ?);

      -- Insert Sales data
      INSERT INTO Sales (CustomerID, ProductID, Quantity, TotalPrice, SaleDate, BusinessID) VALUES
          (1, 1, 2, 999.99 * 2, '2024-04-01', ?),
          (2, 2, 1, 799.99 * 1, '2024-04-02', ?),
          (3, 3, 3, 199.99 * 3, '2024-04-03', ?),
          (4, 4, 2, 299.99 * 2, '2024-04-04', ?),
          (5, 5, 1, 899.99 * 1, '2024-04-05', ?),
          (6, 6, 4, 129.99 * 4, '2024-04-06', ?),
          (7, 7, 2, 449.99 * 2, '2024-04-07', ?),
          (8, 8, 3, 79.99 * 3, '2024-04-08', ?),
          (9, 9, 1, 69.99 * 1, '2024-04-09', ?),
          (10, 10, 2, 349.99 * 2, '2024-04-10', ?),
          (11, 1, 3, 999.99 * 3, '2024-04-11', ?),
          (12, 2, 4, 799.99 * 4, '2024-04-12', ?),
          (13, 3, 1, 199.99 * 1, '2024-04-13', ?),
          (14, 4, 2, 299.99 * 2, '2024-04-14', ?),
          (15, 5, 3, 899.99 * 3, '2024-04-15', ?),
          (16, 6, 4, 129.99 * 4, '2024-04-16', ?),
          (17, 7, 1, 449.99 * 1, '2024-04-17', ?),
          (18, 8, 2, 79.99 * 2, '2024-04-18', ?),
          (19, 9, 3, 69.99 * 3, '2024-04-19', ?),
          (20, 10, 4, 349.99 * 4, '2024-04-20', ?);
    '''
    # Repeating the businessid 40 times
    script_with_values = script.replace('?', str(businessid))
    # Then execute the script
    db.executescript(script_with_values)
    db.commit()
    flash('Data import successful', 'success')
  except db.Error as e:
    error = str(e)
    flash('An error occurred during data import: {}'.format(error), 'error')
  return redirect(url_for('index'))
