import pandas as pd
import numpy as np
import mysql.connector
import settings
from sqlalchemy import create_engine

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
        ID INT PRIMARY KEY AUTO_INCREMENT,
        Invoice VARCHAR(50),
        StockCode VARCHAR(50),
        Description VARCHAR(255),
        Quantity INT,
        InvoiceDate DATETIME,
        Price FLOAT,
        CustomerID INT,
        Country VARCHAR(50)
    );
""")

# Truncate 'customers' table
mycursor.execute("""
    TRUNCATE TABLE customers;
""")
# Truncate 'products' table
mycursor.execute("""
    TRUNCATE TABLE products;
""")
# Truncate 'sales' table
mycursor.execute("""
    TRUNCATE TABLE sales;
""")

# Create Database Connection using SQLAlchemy with MySQL Connector backend
engine = create_engine(f"mysql+mysqlconnector://{settings.USER}:{settings.PASSWORD}@{settings.HOST}/{settings.DATABASE}")

# Read data from online_retail_II.xlsx - Contains 2 sheets: Year 2009-2010 and Year 2010-2011
df_Y0910 = pd.read_excel('online_retail_II.xlsx', sheet_name='Year 2009-2010', parse_dates=['InvoiceDate'])
df_Y1011 = pd.read_excel('online_retail_II.xlsx', sheet_name='Year 2010-2011', parse_dates=['InvoiceDate'])

# Combine data into single df
df_combined = pd.concat([df_Y0910, df_Y1011], ignore_index=True)

# Ensure all alphanumeric StockCodes are uppercase
df_combined['StockCode'] = df_combined['StockCode'].str.upper()

# Define function to process dataframe for each table
def process_df(df, columns, na_columns, dup_columns, mapping, table_name, engine, chunksize=250):
    df = df[columns]
    df = df.dropna(subset=na_columns)
    if dup_columns:  # only drop duplicates if dup_columns is not empty
        df.drop_duplicates(subset=dup_columns, inplace=True)
    df.rename(columns=mapping, inplace=True)

    # Write data to SQL in chunks
    chunks = [df[i:i+chunksize] for i in range(0, df.shape[0], chunksize)]

    for chunk in chunks:
        chunk.to_sql(table_name, con=engine, if_exists='append', index=False)

    return df

# Set variables for 'customer' table
customers_columns = ['Customer ID', 'Country']
customers_na_columns = ['Customer ID']
customers_dup_columns = ['Customer ID']

# Column mapping df to 'customer' table
customers_column_mapping = {
    'Customer ID': 'CustomerID',
    'Country': 'Country'
}

# Populate 'customers' table from df
df_customers = process_df(df_combined, customers_columns, customers_na_columns,
                          customers_dup_columns, customers_column_mapping, 'customers', engine)

# Set variables for 'products' table
products_columns = ['StockCode', 'Description']
products_na_columns = ['StockCode']
products_dup_columns = ['StockCode']

# Column mapping df to 'products' table
products_column_mapping = {
    'StockCode': 'StockCode',
    'Description': 'Description'
}

# Populate 'products' table from df
df_products = process_df(df_combined, products_columns, products_na_columns,
                         products_dup_columns, products_column_mapping, 'products', engine)

# Set variables for 'sales' table
sales_columns = ['Invoice','StockCode', 'Description', 'Quantity', 'InvoiceDate',
                 'Price', 'Customer ID', 'Country']
sales_na_columns = ['Customer ID']
sales_dup_columns = []

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

# Populate 'sales' table from df
df_sales = process_df(df_combined, sales_columns, sales_na_columns, sales_dup_columns,
                      sales_column_mapping, 'sales', engine)

# Add foreign key constraints
mycursor.execute("""
    ALTER TABLE sales
    ADD CONSTRAINT sales_ibfk_1
    FOREIGN KEY (CustomerID)
    REFERENCES customers (CustomerID)
""")

mycursor.execute("""
    ALTER TABLE sales
    ADD CONSTRAINT sales_ibfk_2
    FOREIGN KEY (StockCode)
    REFERENCES products (StockCode)
""")

mycursor.close()