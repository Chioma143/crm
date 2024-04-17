-- User Table
CREATE TABLE User (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Username VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Password VARCHAR(100) NOT NULL,
    UserType TEXT NOT NULL
);

-- Company Table
CREATE TABLE Company (
    CompanyID INTEGER PRIMARY KEY AUTOINCREMENT,
    CompanyName VARCHAR(100) NOT NULL,
    Industry VARCHAR(100),
    Location VARCHAR(100),
    UserID INTEGER,
    FOREIGN KEY (UserID) REFERENCES User(UserID)
);

-- Product Table
CREATE TABLE Product (
    ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProductName VARCHAR(100) NOT NULL,
    Description TEXT,
    Category VARCHAR(50),
    CompanyID INTEGER,
    FOREIGN KEY (CompanyID) REFERENCES Company(CompanyID)
);

-- Price Table
CREATE TABLE Price (
    PriceID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProductID INTEGER,
    Price DECIMAL(10, 2) NOT NULL,
    Currency VARCHAR(3) NOT NULL,
    Date DATE NOT NULL,
    CompetitorName VARCHAR(100),
    CompetitorPrice DECIMAL(10, 2),
    CompetitorURL VARCHAR(255),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);

-- Competitor Table
CREATE TABLE Competitor (
    CompetitorID INTEGER PRIMARY KEY AUTOINCREMENT,
    CompetitorName VARCHAR(100) NOT NULL,
    Industry VARCHAR(100),
    Location VARCHAR(100)
);
