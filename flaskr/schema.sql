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


INSERT INTO User (Username, Email, Password, UserType) VALUES
('chi', 'chi@mail.com', 'scrypt:32768:8:1$I5fZkVfmfrXpRZ8o$954ec06c111d8242f9de2f8766d017c7552e4ed4756c373b33d2527299e2f49dc05d586f128dae478af8c4573dc9d898c67eaea48f4b393b327ce1da764befe0', 'Admin'),
('john_doe', 'john@example.com', 'scrypt:32768:8:1$I5fZkVfmfrXpRZ8o$954ec06c111d8242f9de2f8766d017c7552e4ed4756c373b33d2527299e2f49dc05d586f128dae478af8c4573dc9d898c67eaea48f4b393b327ce1da764befe0', 'Admin'),
('jane_smith', 'jane@example.com', 'scrypt:32768:8:1$I5fZkVfmfrXpRZ8o$954ec06c111d8242f9de2f8766d017c7552e4ed4756c373b33d2527299e2f49dc05d586f128dae478af8c4573dc9d898c67eaea48f4b393b327ce1da764befe0', 'Manager'),
('david_williams', 'david@example.com', 'scrypt:32768:8:1$I5fZkVfmfrXpRZ8o$954ec06c111d8242f9de2f8766d017c7552e4ed4756c373b33d2527299e2f49dc05d586f128dae478af8c4573dc9d898c67eaea48f4b393b327ce1da764befe0', 'Viewer'),
('emma_jones', 'emma@example.com', 'scrypt:32768:8:1$I5fZkVfmfrXpRZ8o$954ec06c111d8242f9de2f8766d017c7552e4ed4756c373b33d2527299e2f49dc05d586f128dae478af8c4573dc9d898c67eaea48f4b393b327ce1da764befe0', 'Admin'),
('michael_brown', 'michael@example.com', 'scrypt:32768:8:1$I5fZkVfmfrXpRZ8o$954ec06c111d8242f9de2f8766d017c7552e4ed4756c373b33d2527299e2f49dc05d586f128dae478af8c4573dc9d898c67eaea48f4b393b327ce1da764befe0', 'Manager'),
('sarah_taylor', 'sarah@example.com', 'scrypt:32768:8:1$I5fZkVfmfrXpRZ8o$954ec06c111d8242f9de2f8766d017c7552e4ed4756c373b33d2527299e2f49dc05d586f128dae478af8c4573dc9d898c67eaea48f4b393b327ce1da764befe0', 'Viewer'),
('chris_miller', 'chris@example.com', 'scrypt:32768:8:1$I5fZkVfmfrXpRZ8o$954ec06c111d8242f9de2f8766d017c7552e4ed4756c373b33d2527299e2f49dc05d586f128dae478af8c4573dc9d898c67eaea48f4b393b327ce1da764befe0', 'Admin'),
('lisa_wilson', 'lisa@example.com', 'scrypt:32768:8:1$I5fZkVfmfrXpRZ8o$954ec06c111d8242f9de2f8766d017c7552e4ed4756c373b33d2527299e2f49dc05d586f128dae478af8c4573dc9d898c67eaea48f4b393b327ce1da764befe0', 'Manager'),
('peter_jackson', 'peter@example.com', 'scrypt:32768:8:1$I5fZkVfmfrXpRZ8o$954ec06c111d8242f9de2f8766d017c7552e4ed4756c373b33d2527299e2f49dc05d586f128dae478af8c4573dc9d898c67eaea48f4b393b327ce1da764befe0', 'Viewer'),
('amy_thompson', 'amy@example.com', 'scrypt:32768:8:1$I5fZkVfmfrXpRZ8o$954ec06c111d8242f9de2f8766d017c7552e4ed4756c373b33d2527299e2f49dc05d586f128dae478af8c4573dc9d898c67eaea48f4b393b327ce1da764befe0', 'Admin');


INSERT INTO Company (CompanyName, Industry, Location, UserID) VALUES
('ABC Ventures', 'Technology', 'Lagos, Nigeria', 1),
('XYZ Solutions', 'Finance', 'Abuja, Nigeria', 2),
('Tech Innovators Ltd', 'Technology', 'Port Harcourt, Nigeria', 3),
('Global Services Ltd', 'Consulting', 'London, UK', 4),
('Nigeria Motors', 'Automobile', 'Kano, Nigeria', 5),
('Giga Tech', 'Technology', 'Manchester, UK', 6),
('Financial Experts Ltd', 'Finance', 'Ibadan, Nigeria', 7),
('Green Energy Ltd', 'Renewable Energy', 'Birmingham, UK', 8),
('Swift Logistics', 'Transportation', 'Kaduna, Nigeria', 9),
('Blue Chips Ltd', 'Finance', 'Liverpool, UK', 10),
('Dynamic Solutions', 'Technology', 'Lagos, Nigeria', 1),
('Secure Bankers', 'Finance', 'Abuja, Nigeria', 2),
('Innovate Tech Ltd', 'Technology', 'Port Harcourt, Nigeria', 3),
('Consultancy Pro', 'Consulting', 'Manchester, UK', 4),
('Naija Auto', 'Automobile', 'Kano, Nigeria', 5),
('TechGenius', 'Technology', 'London, UK', 6),
('Wealth Management Ltd', 'Finance', 'Ibadan, Nigeria', 7),
('Eco Power Ltd', 'Renewable Energy', 'Birmingham, UK', 8),
('Express Logistics', 'Transportation', 'Kaduna, Nigeria', 9),
('Vanguard Financials', 'Finance', 'Liverpool, UK', 10),
('Wealth Builders Ltd', 'Finance', 'Lagos', 10),
('Innovative Solutions', 'Technology', 'Lagos', 1),
('Global Finance', 'Finance', 'Abuja', 2),
('TechSavvy Ltd', 'Technology', 'Port Harcourt', 3),
('Consultancy Experts', 'Consulting', 'Lagos', 4),
('City Auto', 'Automobile', 'Kano', 5),
('TechMaster', 'Technology', 'Abuja', 6),
('Financial Pros Ltd', 'Finance', 'Lagos', 7),
('EcoTech Solutions', 'Renewable Energy', 'Ibadan', 8),
('Speedy Logistics', 'Transportation', 'Kaduna', 9),
('Financial Alliance Ltd', 'Finance', 'Lagos', 10);


INSERT INTO Product (ProductName, Description, Category, CompanyID) VALUES
('Tasty Burger', 'Delicious beef burger with cheese and fries', 'Food', 1),
('Cozy Coffee Mug', 'A warm cup of coffee to start your day', 'Beverage', 2),
('Comfy T-Shirt', 'Soft cotton t-shirt for everyday wear', 'Clothing', 3),
('Stylish Sunglasses', 'Fashionable shades to protect your eyes', 'Accessories', 4),
('Soothing Lavender Candle', 'Calming aroma to relax and unwind', 'Home Decor', 5),
('Classic Leather Wallet', 'Durable wallet to keep your essentials organized', 'Accessories', 6),
('Fresh Fruit Basket', 'Assortment of seasonal fruits for a healthy snack', 'Food', 7),
('Elegant Watch', 'Timeless timepiece to elevate your style', 'Accessories', 8),
('Gourmet Chocolate Box', 'Indulgent chocolates for a sweet treat', 'Food', 9),
('Cozy Throw Blanket', 'Soft and warm blanket for chilly nights', 'Home Decor', 10),
('Gourmet Pizza', 'Delicious pizza with your favorite toppings', 'Food', 1),
('Trendy Sneakers', 'Stylish sneakers for casual outings', 'Footwear', 2),
('Luxurious Silk Scarf', 'Elegant accessory to complement any outfit', 'Clothing', 3),
('Refreshing Green Tea', 'Antioxidant-rich tea for a healthy boost', 'Beverage', 4),
('Artisanal Cheese Platter', 'Variety of cheeses paired with crackers and fruits', 'Food', 5),
('Chic Handbag', 'Fashionable bag to carry your essentials in style', 'Accessories', 6),
('Handcrafted Wooden Bowl', 'Beautifully crafted bowl for serving salads or snacks', 'Home Decor', 7),
('Premium Wine Selection', 'Fine wines from around the world for wine enthusiasts', 'Beverage', 8),
('Exquisite Floral Arrangement', 'Beautiful bouquet of fresh flowers to brighten up any space', 'Home Decor', 9),
('Gourmet Ice Cream Sampler', 'Assorted flavors of artisanal ice cream for dessert lovers', 'Food', 10),
('Artistic Wall Art', 'Unique artwork to adorn your walls and add personality to your home', 'Home Decor', 1),
('Designer Perfume', 'Luxurious fragrance to leave a lasting impression', 'Beauty', 2),
('Handcrafted Jewelry Set', 'Elegant jewelry set for special occasions', 'Accessories', 3),
('Organic Skincare Kit', 'Natural skincare products for a radiant complexion', 'Beauty', 4),
('Aromatic Herbal Tea', 'Herbal infusion for a calming and soothing experience', 'Beverage', 5),
('Cozy Knit Sweater', 'Warm and cozy sweater for chilly days', 'Clothing', 6),
('Designer Leather Bag', 'High-quality leather bag for a sophisticated look', 'Accessories', 7),
('Healthy Snack Pack', 'Nutritious assortment of snacks for guilt-free indulgence', 'Food', 8),
('Charming Picture Frame', 'Decorative frame to showcase your cherished memories', 'Home Decor', 9),
('Luxury Bathrobe', 'Plush bathrobe for a spa-like experience at home', 'Clothing', 10),
('Artisanal Bread Basket', 'Freshly baked assortment of artisanal breads', 'Food', 1),
('Stylish Phone Case', 'Sleek and stylish case to protect your phone', 'Accessories', 2),
('Vintage Vinyl Records', 'Classic vinyl records for music enthusiasts', 'Entertainment', 3),
('Aromatic Essential Oils', 'Natural essential oils for aromatherapy and relaxation', 'Home Decor', 4),
('Handmade Pottery Set', 'Unique pottery set for serving or display', 'Home Decor', 5),
('Designer Silk Tie', 'Luxurious silk tie to complete your formal look', 'Clothing', 6),
('Artisanal Pasta Sampler', 'Variety of artisanal pasta shapes for pasta lovers', 'Food', 7),
('Designer Sunglasses', 'High-end sunglasses for a stylish sun protection', 'Accessories', 8),
('Wholesome Granola Bars', 'Healthy snack bars for on-the-go energy', 'Food', 9),
('Organic Cotton Bedding', 'Soft and sustainable bedding for a comfortable sleep', 'Home Decor', 10),
('Premium Leather Jacket', 'Timeless leather jacket for a rugged yet stylish look', 'Clothing', 1),
('Designer Wristwatch', 'Luxurious wristwatch to make a statement', 'Accessories', 2),
('Artisanal Cheeseboard', 'Gourmet cheese selection served on a wooden board', 'Food', 3),
('Soothing Himalayan Salt Lamp', 'Natural salt lamp for a calming ambiance', 'Home Decor', 4),
('Gourmet Charcuterie Platter', 'Deluxe assortment of cured meats and cheeses', 'Food', 5),
('Aromatic Bath Bombs', 'Fizzy bath bombs for a luxurious bath experience', 'Beauty', 6),
('Vintage-inspired Wall Clock', 'Antique-style wall clock to add character to your home', 'Home Decor', 7),
('Designer Leather Belt', 'High-quality leather belt for a polished look', 'Accessories', 8),
('Artisanal Olive Oil Set', 'Premium olive oil varieties for cooking and dipping', 'Food', 9),
('Refreshing Coconut Water', 'Natural coconut water for hydration and refreshment', 'Beverage', 10);
