# Load necessary libraries
library(hoopR)

# Fetch the latest NBA play-by-play data
nba_data <- hoopR::load_nba_pbp()

# View the structure of the data
str(nba_data)

# View the first few rows to see sample data
head(nba_data)

# Check column names to see all available columns
colnames(nba_data)


# Load the necessary packages
library(hoopR)
library(jsonlite)  # For saving data as JSON

# Fetch the latest NBA play-by-play data (adjust the year range if needed)
nba_data <- hoopR::load_nba_pbp(2023)  # Fetching data for 2023 season only for simplicity

# Select relevant columns (based on available columns in hoopR)
nba_data <- nba_data[, c("game_play_number", "text", "home_score", "away_score", 
                         "period_display_value", "clock_display_value", 
                         "team_id", "athlete_id_1", "score_value", 
                         "away_team_name", "home_team_name")]

# Save the data to a JSON file
write_json(nba_data, path = "nba_data.json")

