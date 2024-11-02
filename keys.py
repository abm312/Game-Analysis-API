import time
from nba_api.live.nba.endpoints import playbyplay, scoreboard

# Function to get the current game ID for a live or upcoming game
def get_live_game_id():
    games = scoreboard.ScoreBoard().get_dict()['scoreboard']['games']
    for game in games:
        if game['gameStatus'] == 2:  # 2 means the game is live
            return game['gameId']
    return None

# Function to print keys for each play in a live game
def inspect_play_keys(game_id):
    # Fetch the play-by-play data
    pbp = playbyplay.PlayByPlay(game_id).get_dict()
    
    # Check if 'game' and 'actions' keys are available in response
    if 'game' in pbp and 'actions' in pbp['game']:
        plays = pbp['game']['actions']
        print("Printing keys for each play:")
        
        for i, play in enumerate(plays[:10]):  # Limiting to first 10 plays for brevity
            print(f"Play {i + 1} keys: {play.keys()}")
            print(play)  # Optionally, print the entire play data to see values
            print("-" * 40)
    else:
        print("No play-by-play data available.")

def main():
    game_id = get_live_game_id()
    if game_id:
        print(f"Inspecting play keys for live game ID: {game_id}")
        inspect_play_keys(game_id)
    else:
        print("No live game found.")

if __name__ == "__main__":
    main()
