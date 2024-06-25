from urllib import response
import requests
from bs4 import BeautifulSoup
import csv
import os
import re
import time


# Function to download a file given its URL and filename
def download_file(url, filename):
    response = requests.get(url)
    with open(filename, "wb") as f:
        f.write(response.content)


# Function to extract data from a webpage and save it as a CSV file
def extract_and_save_data(url, csv_filename):
    # Fetch the webpage content
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all <table> elements on the webpage
    tables = soup.find_all("table")

    # Extract data from each table
    all_data = []
    for table in tables:
        # Find all rows (<tr>) within the table
        rows = table.find_all("tr")
        
        # Determine column names dynamically
        column_names = [header.get_text(strip=True) for header in rows[0].find_all(["th", "td"])]

        # Extract data from each row
        table_data = []
        for row in rows[1:]:
            # Find all cells (<td>) within the row
            cells = row.find_all(["td", "th"])
            # Extract text from each cell
            row_data = [cell.get_text(strip=True) for cell in cells]
            # Append the extracted data to the list
            table_data.append(row_data)

        # Combine column names with data
        table_data_with_columns = [column_names] + table_data
        all_data.extend(table_data_with_columns)

    # Write data to CSV file
    with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(all_data)

    print(f"Data extracted from {url} and saved to {csv_filename}")


# URL of the webpage containing links to individual data pages
main_url = "https://ncua.gov/analysis/cuso-economic-data/credit-union-bank-rates"

# Directory to save the downloaded CSV files
download_dir = "bank-rates/downloaded_csv_files"

# Create download directory if it doesn't exist
if not os.path.exists(download_dir):
    os.makedirs(download_dir)


# Fetch the webpage content
response = requests.get(main_url)
soup = BeautifulSoup(response.text, "html.parser")

# Find all links on the webpage
links = soup.find_all("a")

# Extract links to individual data pages
data_page_links = [link.get("href") for link in links if link.get("href") and "/analysis/cuso-economic-data/credit-union-bank-rates" in link.get("href")]

# Iterate over each data page link, extract data, and save to CSV file
for data_page_link in data_page_links:
    data_page_url = f"https://www.ncua.gov{data_page_link}"
    match = re.search(r'/credit-union-and-bank-rates-(\d{4})-q(\d)', data_page_link)
    if match:
        year = match.group(1)
        quarter = match.group(2)
        csv_filename = os.path.join(download_dir, f"credit_union_and_bank_rates_{year}_q{quarter}.csv")
        extract_and_save_data(data_page_url, csv_filename)

    # Pause for a few seconds before processing the next page
    time.sleep(3)