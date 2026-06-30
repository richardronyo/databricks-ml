from rpy2.robjects import r, pandas2ri
from rpy2.robjects.conversion import localconverter
import pandas as pd
import numpy as np


def load_new_pbp_data():
    """
    This function will load all the latest WNBA Play-By-Play data  
    """ 
    r('''
        # 1. Set CRAN mirror
        options(repos = c(CRAN = "https://cloud.r-project.org/"))

        # 2. Define packages
        packages <- c("pak", "tictoc", "svglite", "arrow")

        # 3. Install missing packages
        for (pkg in packages) {
            if (!require(pkg, character.only = TRUE)) {
                print(paste("Installing", pkg, "..."))
                install.packages(pkg, dependencies = TRUE)
            } else {
                print(paste(pkg, "is already installed"))
            }
        }

        # 4. Load all packages
        lapply(packages, library, character.only = TRUE)
        print("All packages ready!") 

        # 5. Loading the WeHoop package to get the R Data 
        pak::pak("sportsdataverse/wehoop")
      
        library("wehoop")

        # 6. Getting all the Play-By-Play data
        wnba_pbp <- wehoop::load_wnba_pbp()
    ''')

    wnba_pbp_r = r['wnba_pbp']

    with (pandas2ri.converter).context():
        wnba_pbp = pandas2ri.rpy2py(wnba_pbp_r)


    return wnba_pbp

def load_pbp_db():
    """
    This function loads the current WNBA Play-by-Play data in the database 
    """
    current_pbp = pd.read_csv("data/wnba_raw.csv")
    return current_pbp

def add_new_pbp_data(new_pbp, current_pbp):
    """
    This function updates the Play-by-Play file in the database if there are any new games 
    """
    old_games = current_pbp['game_id'].unique()
    all_games = new_pbp['game_id'].unique()

    games_mask = np.isin(all_games, old_games)
    new_game_ids = all_games[~games_mask]

    new_games = new_pbp[new_pbp['game_id'].isin(new_game_ids)]
    if new_games.empty:
        print("Database is up to date!")
    else:
        print("New games added to Database")

    
if __name__ == "__main__":
    new_pbp = load_new_pbp_data()
    current_pbp = load_pbp_db()

    add_new_pbp_data(new_pbp, current_pbp)