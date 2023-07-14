import logging
import os
import time
from pathlib import Path
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout

# Set constants
SEASONS = list(range(2013, 2024))
DATA_DIR = Path("data")
STANDINGS_DIR = DATA_DIR / "standings"
SCORES_DIR = DATA_DIR / "scores"

# Create required directories if they don't exist
os.makedirs(STANDINGS_DIR, exist_ok=True)
os.makedirs(SCORES_DIR, exist_ok=True)

# Initialize logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)


# Define a function to get HTML from a webpage
def get_html(url, selector, sleep=5, retries=3):
    for i in range(retries):
        time.sleep(sleep * i)
        try:
            with sync_playwright() as p:
                with p.firefox.launch() as browser:
                    page = browser.new_page()
                    page.goto(url)
                    logging.debug(f"Successfully loaded {url}")
                    html = page.inner_html(selector)
                    return html
        except PlaywrightTimeout as e:
            logging.warning(f"Timeout error on {url}: {e}")
            continue
    logging.error(f"Failed to load {url} after {retries} retries")
    return None


# Define a function to scrape a season's standings pages
def scrape_season(season):
    # url for scraping
    url = f"https://www.basketball-reference.com/leagues/NBA_{season}_games.html"
    # where to begin scraping
    html = get_html(url, "#content .filter")
    if not html:
        logging.error(f"Failed to load {url}")
        return
    soup = BeautifulSoup(html, features="html.parser")
    links = soup.find_all("a")
    href = [l["href"] for l in links]
    # save links as standings_pages
    standings_pages = [f"https://basketball-reference.com{l}" for l in href]

    for url in standings_pages:
        save_path = STANDINGS_DIR / (url.split("/")[-1])
        if save_path.exists():
            continue
        html = get_html(url, "#all_schedule")
        if not html:
            continue
        try:
            with open(save_path, "w+", encoding="utf-8") as f:
                f.write(html)
        except Exception as e:
            logging.error(f"Error writing file {save_path}: {e}")

# Scrape standings pages and box scores for each season in SEASONS
for season in SEASONS:
    scrape_season(season)

# Check scraped files
standings_files = os.listdir(STANDINGS_DIR)

def scrape_game(standings_file):
    with open(standings_file, "r") as f:
        html = f.read()

    # parse html
    soup = BeautifulSoup(html, features="html.parser")
    # find all "a" tags
    links = soup.find_all("a")
    # filter for box score links
    box_scores = list(filter(lambda l: l and "boxscore" in l and ".html" in l, (l.get("href") for l in links)))
    box_scores = [f"https://www.basketball-reference.com{l}" for l in box_scores]

    # for loop to scrape box score content and write to file
    for url in box_scores:
        save_path = SCORES_DIR / (url.split("/")[-1])
        if save_path.exists():
            continue

        html = get_html(url, "#content")
        if not html:
            logger.error(f"Failed to retrieve HTML content for URL: {url}")
            continue
        try:
            with open(save_path, "w+", encoding="utf-8") as f:
                f.write(html)
        except Exception as e:
            logger.error(f"Failed to write to file {save_path}. Error: {e}")


# loop through standings_files and scrape score content
# skips any file not .html
standings_files = [s for s in standings_files if ".html" in s]

for f in standings_files:
    filepath = os.path.join(STANDINGS_DIR, f)

    try:
        scrape_game(filepath)
    except Exception as e:
        logger.error(f"Error while scraping file {filepath}. Error: {e}")

