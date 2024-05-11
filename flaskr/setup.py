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
      INSERT INTO Customer (CustomerName, Email, Phone, Location, BusinessID)
      VALUES 
          ('John Smith', 'john.smith@example.com', '+1234567891', 'London', ?),
          ('Mary Johnson', 'mary.johnson@example.com', '+1234567892', 'Manchester', ?),
          ('Michael Williams', 'michael.williams@example.com', '+1234567893', 'Birmingham', ?),
          ('Jennifer Brown', 'jennifer.brown@example.com', '+1234567894', 'Leeds', ?),
          ('Christopher Jones', 'christopher.jones@example.com', '+1234567895', 'Glasgow', ?),
          ('Amanda Davis', 'amanda.davis@example.com', '+1234567896', 'Liverpool', ?),
          ('James Miller', 'james.miller@example.com', '+1234567897', 'Bristol', ?),
          ('Jessica Wilson', 'jessica.wilson@example.com', '+1234567898', 'Edinburgh', ?),
          ('David Martinez', 'david.martinez@example.com', '+1234567899', 'Sheffield', ?),
          ('Linda Taylor', 'linda.taylor@example.com', '+1234567800', 'Newcastle', ?),
          ('Matthew Anderson', 'matthew.anderson@example.com', '+1234567801', 'Cardiff', ?),
          ('Barbara Thomas', 'barbara.thomas@example.com', '+1234567802', 'Belfast', ?),
          ('Richard Jackson', 'richard.jackson@example.com', '+1234567803', 'Dublin', ?),
          ('Sarah White', 'sarah.white@example.com', '+1234567804', 'Aberdeen', ?),
          ('Daniel Harris', 'daniel.harris@example.com', '+1234567805', 'Cambridge', ?),
          ('Nancy Clark', 'nancy.clark@example.com', '+1234567806', 'Oxford', ?),
          ('Karen Lewis', 'karen.lewis@example.com', '+1234567807', 'York', ?),
          ('Mark King', 'mark.king@example.com', '+1234567808', 'Brighton', ?),
          ('Lisa Scott', 'lisa.scott@example.com', '+1234567809', 'Nottingham', ?),
          ('Paul Green', 'paul.green@example.com', '+1234567810', 'Southampton', ?);

      -- Insert Product data
      INSERT INTO Product (ProductName, Description, Category, Currency, Price, BusinessID)
      VALUES 
          ('Apple', 'Fresh red apples', 'Grocery', 'GBP', 1.2, ?),
          ('Toothpaste', 'Mint-flavored toothpaste', 'Health and Beauty', 'GBP', 2.5, ?),
          ('Laptop', '15" Intel Core i7', 'Electronics', 'GBP', 899.99, ?),
          ('Detergent', 'Eco-friendly detergent', 'Household Goods', 'GBP', 5.99, ?),
          ('Banana', 'Ripe yellow bananas', 'Grocery', 'GBP', 0.5, ?),
          ('Shampoo', 'Coconut-scented shampoo', 'Health and Beauty', 'GBP', 4.75, ?),
          ('Smartphone', '6.5" Android smartphone', 'Electronics', 'GBP', 699.99, ?),
          ('Trash Bags', 'Biodegradable trash bags', 'Household Goods', 'GBP', 7.49, ?),
          ('Orange', 'Juicy oranges', 'Grocery', 'GBP', 1, ?),
          ('Conditioner', 'Argan oil conditioner', 'Health and Beauty', 'GBP', 6.25, ?),
          ('Smart Watch', 'Fitness tracking smartwatch', 'Electronics', 'GBP', 129.99, ?),
          ('Dish Soap', 'Lemon-scented dish soap', 'Household Goods', 'GBP', 2.99, ?),
          ('Bread', 'Whole grain bread', 'Grocery', 'GBP', 1.99, ?),
          ('Face Cream', 'Anti-aging face cream', 'Health and Beauty', 'GBP', 12.99, ?),
          ('Bluetooth Speaker', 'Portable Bluetooth speaker', 'Electronics', 'GBP', 39.99, ?),
          ('Laundry Detergent', 'Hypoallergenic laundry detergent', 'Household Goods', 'GBP', 8.99, ?),
          ('Milk', 'Fresh cow milk', 'Grocery', 'GBP', 1.5, ?),
          ('Sunscreen', 'SPF 50 sunscreen lotion', 'Health and Beauty', 'GBP', 9.99, ?),
          ('Headphones', 'Noise-canceling headphones', 'Electronics', 'GBP', 149.99, ?),
          ('Paper Towels', 'Absorbent paper towels', 'Household Goods', 'GBP', 3.49, ?),
          ('Eggs', 'Free-range chicken eggs', 'Grocery', 'GBP', 2.2, ?),
          ('Face Wash', 'Aloe vera face wash', 'Health and Beauty', 'GBP', 5.49, ?),
          ('Digital Camera', '24MP DSLR camera', 'Electronics', 'GBP', 499.99, ?),
          ('Trash Can', 'Stainless steel trash can', 'Household Goods', 'GBP', 19.99, ?),
          ('Cereal', 'Whole grain cereal', 'Grocery', 'GBP', 3.75, ?),
          ('Body Lotion', 'Shea butter body lotion', 'Health and Beauty', 'GBP', 8.99, ?),
          ('Smart Thermostat', 'WiFi-enabled smart thermostat', 'Electronics', 'GBP', 149.99, ?),
          ('All-Purpose Cleaner', 'Multi-surface cleaner', 'Household Goods', 'GBP', 4.99, ?),
          ('Orange Juice', 'Freshly squeezed orange juice', 'Grocery', 'GBP', 2.99, ?),
          ('Lip Balm', 'SPF 15 lip balm', 'Health and Beauty', 'GBP', 1.99, ?),
          ('Laptop Stand', 'Adjustable laptop stand', 'Electronics', 'GBP', 24.99, ?),
          ('Trash Bags', 'Recyclable trash bags', 'Household Goods', 'GBP', 6.99, ?);

      -- Insert Sales data
      INSERT INTO Sales (CustomerID, ProductID, Quantity, TotalPrice, SaleDate, BusinessID) VALUES
          (5, 1, 3, 0, '2024-04-01', ?),
          (7, 2, 2, 0, '2024-04-02', ?),
          (3, 3, 4, 0, '2024-04-03', ?),
          (15, 4, 3, 0, '2024-04-04', ?),
          (11, 5, 2, 0, '2024-04-05', ?),
          (8, 6, 5, 0, '2024-04-06', ?),
          (20, 7, 3, 0, '2024-04-07', ?),
          (13, 8, 4, 0, '2024-04-08', ?),
          (18, 9, 2, 0, '2024-04-09', ?),
          (10, 10, 3, 0, '2024-04-10', ?),
          (12, 1, 4, 0, '2024-04-11', ?),
          (6, 2, 5, 0, '2024-04-12', ?),
          (17, 3, 2, 0, '2024-04-13', ?),
          (14, 4, 3, 0, '2024-04-14', ?),
          (9, 5, 4, 0, '2024-04-15', ?),
          (2, 6, 5, 0, '2024-04-16', ?),
          (19, 7, 2, 0, '2024-04-17', ?),
          (4, 8, 3, 0, '2024-04-18', ?),
          (16, 9, 4, 0, '2024-04-19', ?),
          (1, 10, 5, 0, '2024-04-20', ?),
          (7, 11, 3, 0, '2024-04-21', ?),
          (9, 12, 2, 0, '2024-04-22', ?),
          (11, 13, 4, 0, '2024-04-23', ?),
          (13, 14, 3, 0, '2024-04-24', ?),
          (15, 15, 2, 0, '2024-04-25', ?),
          (17, 16, 5, 0, '2024-04-26', ?),
          (19, 17, 3, 0, '2024-04-27', ?),
          (1, 18, 4, 0, '2024-04-28', ?),
          (3, 19, 2, 0, '2024-04-29', ?),
          (5, 20, 3, 0, '2024-04-30', ?);
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
