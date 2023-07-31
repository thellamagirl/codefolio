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

# Read data from online_retail_II.xlsx - Contains 2 sheets: Year 2009-2010 and Year 2010-2011
df_Y0910 = pd.read_excel("online_retail_II_Year 2009-2010", parse_dates=['InvoiceDate'])
df_Y1011 = pd.read_excel("online_retail_II_Year 2010-2011", parse_dates=['InvoiceDate'])

# Combine data into single df
df_combined = pd.concat([df_Y0910, df_Y1011], ignore_index=True)

# Column mapping df to 'customer' table
customers_column_mapping = {
    'Customer ID': 'CustomerID',
    'Country': 'Country'
}

# Insert data into 'customers' table using column mapping
df_customers = df_combined[['Customer ID', 'Country']]
# Remove duplicate customers if needed
df_customers.drop_duplicates(subset='Customer ID', inplace=True) 
# Convert to sql and insert into 'customers' table in 'salesdb'
df_customers.to_sql('customers', salesdb, if_exists='append', index=False, columns=customers_column_mapping)

# Column mapping df to 'products' table
products_column_mapping = {
    'StockCode': 'StockCode',
    'Description': 'Description'
}

# Insert data into 'products' table using column mapping
df_products = df_combined[['StockCode', 'Description']]
# Remove duplicate products if needed
df_products.drop_duplicates(subset='StockCode', inplace=True)
# Convert to sql and insert into 'products' table in 'salesdb'
df_products.to_sql('products', salesdb, if_exists='append', index=False, columns=products_column_mapping)

# Column mapping df to 'sales' table
sales_column_mapping = {
    'Invoice': 'Invoice',
    'StockCode': 'StockCode',
    'Description': 'Description',
    'Quantity': 'Quantity',
    'InvoiceDate': 'InvoiceDate',
    'Price': 'Price',
    'Customer ID': 'CustomerID',
    'Country': 'Country'
}

# Insert data into 'sales' table using column mapping
df_sales = df_combined[['Invoice','StockCode', 'Description', 'Quantity', 'InvoiceDate', 'Price', 'Customer ID', 'Country']]
# Convert to sql and insert into 'sales' table in 'salesdb'
df_sales.to_sql('sales', salesdb, if_exists='append', index=False, columns=sales_column_mapping)

