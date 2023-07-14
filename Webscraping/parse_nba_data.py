import os
import pandas as pd
from bs4 import BeautifulSoup
from pathlib import Path

# Set constants
DATA_DIR = Path("data")
SCORES_DIR = DATA_DIR / "scores"

box_scores = os.listdir(SCORES_DIR)
box_scores = [os.path.join(SCORES_DIR, f) for f in box_scores if f.endswith(".html")]

def parse_html(box_score):
    try:
        with open(box_score, encoding="utf-8") as f:
            html = f.read()
    except FileNotFoundError:
        print(f"File {box_score} not found.")
        return None
    except UnicodeDecodeError:
        print(f"Error decoding file {box_score}.")
        return None

    try:
        soup = BeautifulSoup(html, features="html.parser")
        # selects tr (table row) tag with class over_header
        # decompose removes it from the html
        [s.decompose() for s in soup.select("tr.over_header")]
        # remove tr thead
        [s.decompose() for s in soup.select("tr.thead")]
        return soup
    except:
        print(f"Error parsing HTML in {box_score}.")
        return None


def read_line_score(soup):
    try:
        # Read line_score table into df
        line_score = pd.read_html(soup.prettify(), flavor='bs4', attrs={"id": "line_score"})[0]

        # Rename columns
        cols = list(line_score.columns)
        cols[0] = "team"
        cols[-1] = "total"
        # assign it back to the columns
        line_score.columns = cols
        # Drop quarter columns
        line_score = line_score[['team', 'total']]

        return line_score
    except ValueError:
        print(f"ValueError: No line_score table found in {SCORES_DIR}. Skipping...")
        return None
    except:
        print(f"Error reading line score for file {SCORES_DIR}. Skipping...")
        return None


def read_stats(soup: BeautifulSoup, team: str, stat: str) -> pd.DataFrame:
    """Reads a stats table from box score HTML page into a pandas DataFrame."""
    try:
        df = pd.read_html(str(soup), attrs={'id': f'box-{team}-game-{stat}'}, index_col=0)[0]
    except ValueError as e:
        raise ValueError(f"Error parsing stats table for {team}: {e}") from None
        
    df = df.apply(pd.to_numeric, errors='coerce')
    df = df.dropna(how='all')
    
    # Clean up column names
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.replace(' ', '_')
    
    # Remove extra columns
    cols_to_drop = [c for c in df.columns if c.startswith('Unnamed')]
    df = df.drop(columns=cols_to_drop)
    
    return df


def read_season_info(soup):
    # select bottom nav container
    nav = soup.select("#bottom_nav_container")[0]
    # find all links in nav
    hrefs = [a["href"] for a in nav.find_all("a")]
    # path for season
    season = os.path.basename(hrefs[1]).split("_")[0]
    return season


base_cols = None
games = []

for box_score in box_scores:
    soup = parse_html(box_score)
    if soup is None:
        continue  # move on to the next box score file
        
    line_score = read_line_score(soup)
    
    if line_score is not None:
        teams = list(line_score["team"])
        
        summaries = []
        for team in teams:
            # read in basic stats table
            basic = read_stats(soup, team, "basic")
            # read in advanced stats table
            advanced = read_stats(soup, team, "advanced")

            # check if "MP" column appears in basic and drop it from advanced
            if "MP" in basic.columns:
                advanced = advanced.drop(columns=["MP"])

            # concat totals from last row of basic df and advanced df into single pd series
            totals = pd.concat([basic.iloc[-1, :], advanced.iloc[-1, :]])
            # rename totals index
            totals.index = totals.index.str.lower()

            # create maximum value for each player
            maxes = pd.concat([basic.iloc[:-1, :].max(), advanced.iloc[:-1, :].max()])
            # rename index
            maxes.index = maxes.index.str.lower() + "_max"

            # concat them together to get a summary
            summary = pd.concat([totals, maxes])
                    
            # Set base columns and drop duplicates
            if base_cols is None:
                base_cols = list(summary.dropna().index.drop_duplicates(keep="first"))
                # remove bpm stat since it isn't in all box scores
                base_cols = [b for b in base_cols if "bpm" not in b]

            summary = summary[base_cols]
            
            # append summary to summaries list
            summaries.append(summary)
    else:
        print(f"Skipping {box_score} due to missing line score table")
        continue  # move on to the next box score file

    # concat summaries into single summary and turn axis
    summary = pd.concat(summaries, axis=1).T
    # concat summary and line summary
    game = pd.concat([summary, line_score], axis=1)
    # assign column for away/home game
    game["home"] = [0, 1]
    # concat team and opponent stats
    game_opp = game.iloc[::-1].reset_index()
    game_opp.columns += "_opp"

    full_game = pd.concat([game, game_opp], axis=1)
    # add season column to full game df
    full_game["season"] = read_season_info(soup)

    # extract game date from the filename and convert to datetime object
    full_game["date"] = pd.to_datetime(os.path.basename(box_score)[:8], format="%Y%m%d")
    
    # add won column to full game df
    full_game["won"] = full_game["total"] > full_game["total_opp"]
    # append full game to games list
    games.append(full_game)

    # print loop progress
    if len(games) % 100 == 0:
        print(f"{len(games)} / {len(box_scores)}")

# concat games together into a single df
games_df = pd.concat(games, ignore_index=True)

# write games data to csv
games_df.to_csv("nba_games.csv")
