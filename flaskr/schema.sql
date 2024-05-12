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
    Email VARCHAR(100) NOT NULL,
    Phone VARCHAR(100) NOT NULL,
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