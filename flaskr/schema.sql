-- User Table
DROP TABLE IF EXISTS User;
CREATE TABLE User (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Username VARCHAR(50) UNIQUE NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Password VARCHAR(200) NOT NULL,
    UserType TEXT NOT NULL,
    BusinessID INTEGER, -- Added column to represent the user's business
    FOREIGN KEY (BusinessID) REFERENCES Business(BusinessID)
);

-- Business Table
DROP TABLE IF EXISTS Business;
CREATE TABLE Business (
    BusinessID INTEGER PRIMARY KEY AUTOINCREMENT,
    BusinessName VARCHAR(100) NOT NULL
);

-- Customer Table
DROP TABLE IF EXISTS Customer;
CREATE TABLE Customer (
    CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
    CustomerName VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(100) NOT NULL,
    Industry VARCHAR(100),
    Location VARCHAR(100),
    BusinessID INTEGER, -- Added column to represent the business that owns the customer
    FOREIGN KEY (BusinessID) REFERENCES Business(BusinessID)
);

-- Product Table
DROP TABLE IF EXISTS Product;
CREATE TABLE Product (
    ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProductName VARCHAR(100) NOT NULL,
    Description TEXT,
    Price DECIMAL(10, 2) NOT NULL,
    Currency VARCHAR(3) NOT NULL,
    Category VARCHAR(50),
    BusinessID INTEGER, -- Added column to represent the business that owns the product
    FOREIGN KEY (BusinessID) REFERENCES Business(BusinessID)
);

-- Sales Table
DROP TABLE IF EXISTS Sales;
CREATE TABLE Sales (
    SaleID INTEGER PRIMARY KEY AUTOINCREMENT,
    CustomerID INTEGER,
    ProductID INTEGER,
    Quantity INTEGER NOT NULL,
    TotalPrice DECIMAL(10, 2) NOT NULL,
    SaleDate DATE NOT NULL,
    BusinessID INTEGER, -- Added column to represent the business that made the sale
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID),
    FOREIGN KEY (BusinessID) REFERENCES Business(BusinessID)
);

-- CRM Table
DROP TABLE IF EXISTS CRM;
CREATE TABLE CRM (
    CRMID INTEGER PRIMARY KEY AUTOINCREMENT,
    CRMName VARCHAR(100) NOT NULL,
    BusinessID INTEGER, -- Added column to represent the business that controls the CRM
    FOREIGN KEY (BusinessID) REFERENCES Business(BusinessID)
);

/* BEGIN TRANSACTION;
INSERT INTO Customer (CustomerName, Email, Phone, Industry, Location, BusinessID)
VALUES 
    ('John Smith', 'john.smith@example.com', '+1234567891', 'Technology', 'London', 1),
    ('Mary Johnson', 'mary.johnson@example.com', '+1234567892', 'Retail', 'Manchester', 1),
    ('Michael Williams', 'michael.williams@example.com', '+1234567893', 'Fashion', 'Birmingham', 1),
    ('Jennifer Brown', 'jennifer.brown@example.com', '+1234567894', 'Technology', 'Liverpool', 1),
    ('Christopher Jones', 'christopher.jones@example.com', '+1234567895', 'Retail', 'Leeds', 1),
    ('Amanda Davis', 'amanda.davis@example.com', '+1234567896', 'Fashion', 'Sheffield', 1),
    ('James Miller', 'james.miller@example.com', '+1234567897', 'Technology', 'Bristol', 1),
    ('Jessica Wilson', 'jessica.wilson@example.com', '+1234567898', 'Retail', 'Glasgow', 1),
    ('David Martinez', 'david.martinez@example.com', '+1234567899', 'Fashion', 'Edinburgh', 1),
    ('Linda Taylor', 'linda.taylor@example.com', '+1234567800', 'Technology', 'Cardiff', 1),
    ('Matthew Anderson', 'matthew.anderson@example.com', '+1234567801', 'Retail', 'Belfast', 1),
    ('Barbara Thomas', 'barbara.thomas@example.com', '+1234567802', 'Fashion', 'Dublin', 1),
    ('Richard Jackson', 'richard.jackson@example.com', '+1234567803', 'Technology', 'Newcastle', 1),
    ('Sarah White', 'sarah.white@example.com', '+1234567804', 'Retail', 'Southampton', 1),
    ('Daniel Harris', 'daniel.harris@example.com', '+1234567805', 'Fashion', 'Brighton', 1),
    ('Nancy Clark', 'nancy.clark@example.com', '+1234567806', 'Technology', 'Cambridge', 1),
    ('Karen Lewis', 'karen.lewis@example.com', '+1234567807', 'Retail', 'Oxford', 1),
    ('Mark King', 'mark.king@example.com', '+1234567808', 'Fashion', 'Norwich', 1),
    ('Lisa Scott', 'lisa.scott@example.com', '+1234567809', 'Technology', 'York', 1),
    ('Paul Green', 'paul.green@example.com', '+1234567810', 'Retail', 'Cardiff', 1);

INSERT INTO Product (ProductName, Description, Price, Currency, Category, BusinessID)
VALUES 
    ('Laptop', 'High-performance laptop with SSD storage', 999.99, 'GBP', 'Electronics', 1),
    ('Smartphone', 'Latest smartphone with advanced camera features', 799.99, 'GBP', 'Electronics', 1),
    ('Wireless Headphones', 'Premium wireless headphones with noise cancellation', 199.99, 'GBP', 'Electronics', 1),
    ('Coffee Machine', 'Espresso machine with built-in grinder', 299.99, 'GBP', 'Kitchen Appliances', 1),
    ('Smart TV', '4K smart TV with HDR support', 899.99, 'GBP', 'Electronics', 1),
    ('Fitness Tracker', 'Waterproof fitness tracker with heart rate monitoring', 129.99, 'GBP', 'Health & Fitness', 1),
    ('Gaming Console', 'Next-gen gaming console with 4K gaming support', 449.99, 'GBP', 'Electronics', 1),
    ('Wireless Router', 'High-speed wireless router with extended range', 79.99, 'GBP', 'Electronics', 1),
    ('Portable Speaker', 'Bluetooth portable speaker with long battery life', 69.99, 'GBP', 'Electronics', 1),
    ('Robot Vacuum Cleaner', 'Smart robot vacuum cleaner with mapping technology', 349.99, 'GBP', 'Home Appliances', 1),
    ('Digital Camera', 'Professional digital camera with interchangeable lenses', 1199.99, 'GBP', 'Electronics', 1),
    ('Electric Toothbrush', 'Electric toothbrush with multiple cleaning modes', 49.99, 'GBP', 'Health & Beauty', 1),
    ('Wireless Mouse', 'Ergonomic wireless mouse for comfortable use', 29.99, 'GBP', 'Electronics', 1),
    ('Blender', 'High-powered blender for making smoothies and shakes', 89.99, 'GBP', 'Kitchen Appliances', 1),
    ('External Hard Drive', 'Portable external hard drive for data backup', 129.99, 'GBP', 'Electronics', 1),
    ('Fitness Watch', 'Smart fitness watch with GPS tracking', 199.99, 'GBP', 'Health & Fitness', 1),
    ('Hair Dryer', 'Professional hair dryer with ion technology', 79.99, 'GBP', 'Health & Beauty', 1),
    ('Air Purifier', 'HEPA air purifier for cleaner indoor air', 149.99, 'GBP', 'Home Appliances', 1),
    ('Electric Kettle', 'Fast-boiling electric kettle for tea and coffee', 39.99, 'GBP', 'Kitchen Appliances', 1),
    ('Wireless Earbuds', 'True wireless earbuds with noise isolation', 149.99, 'GBP', 'Electronics', 1);

INSERT INTO Sales (CustomerID, ProductID, Quantity, TotalPrice, SaleDate, BusinessID) VALUES
    (1, 1, 2, 1999.98, '2024-04-01', 1),
    (2, 2, 1, 799.99, '2024-04-02', 1),
    (3, 3, 3, 599.97, '2024-04-03', 1),
    (4, 4, 2, 599.98, '2024-04-04', 1),
    (5, 5, 1, 899.99, '2024-04-05', 1),
    (6, 6, 4, 519.96, '2024-04-06', 1),
    (7, 7, 2, 899.98, '2024-04-07', 1),
    (8, 8, 3, 239.97, '2024-04-08', 1),
    (9, 9, 1, 129.99, '2024-04-09', 1),
    (10, 10, 2, 899.98, '2024-04-10', 1),
    (11, 1, 3, 2399.97, '2024-04-11', 1),
    (12, 2, 4, 3199.96, '2024-04-12', 1),
    (13, 3, 1, 199.99, '2024-04-13', 1),
    (14, 4, 2, 599.98, '2024-04-14', 1),
    (15, 5, 3, 2699.97, '2024-04-15', 1),
    (16, 6, 4, 479.96, '2024-04-16', 1),
    (17, 7, 1, 179.99, '2024-04-17', 1),
    (18, 8, 2, 159.98, '2024-04-18', 1),
    (19, 9, 3, 299.97, '2024-04-19', 1),
    (20, 10, 4, 519.96, '2024-04-20', 1);


COMMIT;
 */