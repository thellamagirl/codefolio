import pandas as pd
import numpy as np
import mysql.connector
import settings

# Create Database Connection
salesdb = mysql.connector.connect(
    host=settings.HOST,
    user=settings.USER,
    password=settings.PASSWORD
)

mycursor = salesdb.cursor()

# Create the 'salesdb' database
mycursor.execute("CREATE DATABASE IF NOT EXISTS salesdb")


# Select 'salesdb' to use during table creation
mycursor.execute("USE salesdb")


# Create tables
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        CustomerID INT PRIMARY KEY, 
        Country VARCHAR(100)
    );                 
""")

mycursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        StockCode VARCHAR(50) PRIMARY KEY,
        Description VARCHAR(255)
    );
""")

mycursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        Invoice INT PRIMARY KEY,
        StockCode VARCHAR(50),
        Description VARCHAR(255),
        Quantity INT,
        InvoiceDate DATETIME,
        Price FLOAT,
        CustomerID INT,
        Country VARCHAR(50),
        FOREIGN KEY (CustomerID) REFERENCES customers(CustomerID),
        FOREIGN KEY (StockCode) REFERENCES products(StockCode)
    );
""")