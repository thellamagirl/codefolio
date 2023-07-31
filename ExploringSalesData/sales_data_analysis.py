# Imports
import pandas as pd
import numpy as np
import mysql.connector
import settings

# Create Database
salesdb = mysql.connector.connect(
  host=settings.HOST,
  user=settings.USER,
  password=settings.PASSWORD
)

mycursor = salesdb.cursor()

mycursor.execute("CREATE DATABASE salesdatabase")

