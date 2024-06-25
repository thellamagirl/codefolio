from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import csv
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def scrape_credit_unions():
    # Initialize Chrome webdriver
    driver = webdriver.Chrome()

    # Load the webpage
    driver.get("https://mapping.ncua.gov/ResearchCreditUnion")

    # Find the element containing the specified text
    specific_text_element = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'OR: To search for a credit union, enter information into one or more fields and click the FIND button.')]")))
    
    # Click on the element to open the search area
    specific_text_element.click()

    # Wait for the arrow to open the dropdown
    arrow_to_open_dropdown = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='mat-select-50']/div/div[2]")))
    arrow_to_open_dropdown.click()

    # Wait for the state select dropdown to be visible
    state_select_dropdown = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//mat-select[@formcontrolname='state']")))

    # Click on the state select dropdown to open it
    state_select_dropdown.click()

    # Wait for "Utah" option to be visible within the state select dropdown
    utah_option = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(@class, 'mat-option-text') and text()='Utah']")))

    # Click on "Utah" within the state select dropdown
    utah_option.click()

    # Click on "FIND" to initiate the search
    find_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'FIND')]")))
    find_button.click()

    # Wait for the search results to load
    time.sleep(5)

    # Parse the HTML content
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Extract charter numbers of credit unions
    charter_numbers = [row.find("td", {"class": "mat-cell cdk-cell cdk-column-charterNumber ng-star-inserted"}).text.strip() for row in soup.find_all("tr", {"class": "mat-row ng-star-inserted"})]
    
    # Construct URLs for credit union details pages
    credit_union_urls = [f"https://mapping.ncua.gov/CreditUnionDetails/{charter}" for charter in charter_numbers]

    # Close the webdriver
    driver.quit()

    return credit_union_urls


def scrape_credit_union_details(url):
    # Initialize Chrome webdriver
    driver = webdriver.Chrome()

    # Load the credit union details page
    driver.get(url)

    # Wait for the page to load
    time.sleep(5)

    # Parse the HTML content
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Extract relevant details from the credit union details page
    table = soup.find("table", {"class": "table-details"})

    # Initialize dictionary to store details
    details = {}

    # Iterate through table rows to extract data
    for row in table.find_all("tr"):
        header_cell = row.find("td", {"class": "dvHeader"})
        value_cell = row.find("td", {"class": None})  # Assuming value cells don't have a class
        
        if header_cell and value_cell:
            header = header_cell.text.strip()
            value = value_cell.text.strip()
            details[header] = value

    # Close the webdriver
    driver.quit()

    return details



def main():
    # Scrape credit union URLs for Utah
    credit_union_urls = scrape_credit_unions()

    # Create or open the CSV file to append data
    with open("utah_credit_unions.csv", "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["Credit Union Name", "Charter Number", "Credit Union Type", "Credit Union Status", "Corporate Credit Union", "Credit Union Charter Year", "Current Charter Issue Date", "Date Insured", "Charter State", "Region", "Field of Membership Type", "Low Income Designation", "Member of FHLB", "Assets", "Peer Group", "Number of Members", "Main Office Address", "City, State Zip code", "Country", "County", "Phone", "Website", "CEO/Manager"])
        
        # Write header row if file is empty
        if csvfile.tell() == 0:
            writer.writeheader()

        # Scrape details for each credit union and append to CSV
        for url in credit_union_urls:
            details = scrape_credit_union_details(url)
            writer.writerow(details)

if __name__ == "__main__":
    main()
