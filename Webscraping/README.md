# SwishStats: NBA Score Web Scraper and Analysis Tool

## Overview

SwishStats: NBA Score Web Scraper and Analysis Tool is a Python-based web scraping project that collects and extracts basic and advanced team statistics from the Basketball-Reference website. The project utilizes the BeautifulSoup and Playwright libraries to scrape 10 years' worth of NBA basketball data, providing valuable insights into team performance and trends over time.

## Features

- Scrapes NBA team statistics for multiple seasons, including regular season and playoff data.
- Extracts a wide range of basic team statistics such as points scored, rebounds, assists,    field goal percentage, etc.
- Retrieves advanced team statistics like offensive rating, defensive rating, net rating, effective field goal percentage, etc.
- Organizes the collected data into a structured format (CSV) for further analysis and visualization.

## Installation and Setup

1. Clone the project repository to your local machine:

   ```bash
   git clone https://github.com/thellamagirl/stunning-giggle/tree/main/WebScraping
   ``` 

2. Navigate to the project directory:

   ```bash
   cd WebScraping
   ```

3. Create and activate a virtual environment to isolate project dependencies:

   ```bash
   python3 -m venv myenv    # Create a virtual environment
   source myenv/bin/activate    # Activate the virtual environment
   ```

   This step is optional but recommended to keep your project dependencies separate from other Python installations on your system.

4. Install the required libraries and dependencies using `pip` and the provided `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

   This command will install all the necessary packages and their specified versions.

## Usage

5. Scrape the data:

   ```bash
   python get_nba_data.py
   ```
   This script uses web scraping techniques and the Playwright library to scrape NBA standings and box score data from the basketball-reference.com website. It retrieves the HTML content, parses it, and saves the relevant data into separate directories for further analysis. The logging functionality is implemented to track the scraping process and handle potential errors. 
   
   While this script focuses on 2013-2023 NBA basketball seasons, any range would work to suit your needs. Update the SEASONS constant to desired season range.


6. Parse & organize the data:

   ```bash
   python parse_nba_data.py
   ```
   This script uses web scraping techniques to extract NBA box score data from HTML files. It leverages various functions to parse the HTML content, extract relevant tables, clean and organize the data, and store it in a structured format for further analysis and visualization.

## Configuration

SwishStats: NBA Score Web Scraper and Analysis Tool does not require any additional configuration files or settings.

## Contributing

### Bug Reports and Feature Requests
If you encounter a bug or have a feature request, please check the existing issues on the project's GitHub repository to see if it has already been reported. If not, you can open a new issue with a clear and descriptive title, along with a detailed explanation of the problem or feature you'd like to see. Provide any relevant information, such as error messages or examples, that can help in understanding and reproducing the issue.

## Data Source

The data used in this project was obtained through web scraping from Basketball-Reference website. Please note that the web scraping process followed the guidelines provided in the website's `robots.txt` file, respecting the disallowed directories and URLs. The project aims to demonstrate how to scrape and interpret basic and advanced basketball stats, and the scraped data is utilized for informational and educational purposes only.

## License

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

## Acknowledgments

This project was created based on the NBA Games Project Walkthrough by Dataquest. The walkthrough provided valuable guidance and served as a foundation for this project. I want to express my gratitude to Dataquest for sharing their expertise and resources. The GitHub repo for the walkthrough can be found at https://github.com/dataquestio/project-walkthroughs/tree/master/nba_games

## Contact

You can contact me at thellamagirl@outlook.com

