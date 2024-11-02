


import openai
import time
from nba_api.live.nba.endpoints import scoreboard, playbyplay

# Set up OpenAI API key
openai.api_key = "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"

# Function to get the current game ID for a live game
def get_live_game_id():
    games = scoreboard.ScoreBoard().get_dict()['scoreboard']['games']
    for game in games:
        if game['gameStatus'] == 2:  # 2 means the game is live
            return game['gameId'], game['homeTeam']['teamName'], game['awayTeam']['teamName']
    return None, None, None

def format_prompt(play):
    # Collecting additional context for player names and play details
    player_name = play.get('playerName', 'Unknown Player')
    action_type = play.get('actionType', 'action')
    team = play.get('teamTricode', 'Unknown Team')
    possession = "has possession" if play.get('possession') else "does not have possession"

    # Creating a detailed, confident prompt with percentages and no disclaimers
    prompt = (
        f"In the {play['period']} with {play['clock']} remaining, "
        f"{team}'s {player_name} performs a {action_type}. "
        f"{play['description']} Current score: {play['scoreHome']} - {play['scoreAway']}. "
        f"{team} currently {possession}. "
        "Based on the real-time data provided through nba_api, restate the current play information briefly, and then "
        "predict the likelihood of each team winning this game in percentage terms. "
        "Use only the current game information to make your prediction, and express it confidently in terms of percentages for each team. "
        "Avoid any disclaimers or statements about uncertainty—just give the current win probability as best as possible."
    )
    return prompt



# Function to get GPT prediction
def get_gpt_prediction(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=250
    )
    return response.choices[0].message['content'].strip()

# # Main function to simulate a live game
# def main():
#     game_id, home_team, away_team = get_live_game_id()
    
#     if not game_id:
#         print("No live game found.")
#         return
    
#     print(f"Simulating Live Game between {home_team} and {away_team}")
#     print("=" * 60)

#     interval = 5  # Define an interval for checking updates
    
#     while True:
#         # Fetch the latest play-by-play data
#         pbp = playbyplay.PlayByPlay(game_id).get_dict()
        
#         # Check if 'game' and 'actions' keys are available in response
#         if 'game' in pbp and 'actions' in pbp['game']:
#             plays = pbp['game']['actions']
            
#             # Filter plays by the interval and analyze each selected play
#             for i, play in enumerate(plays[-interval:]):  # Analyze the last few plays
#                 prompt = format_prompt(play)
#                 prediction = get_gpt_prediction(prompt)
                
#                 # Display each play and the prediction
#                 print(f"Play {i + 1}:")
#                 print(f"Prediction: {prediction}")
#                 print("\n" + "-" * 60 + "\n")
        
#         # Pause for a while before checking for new plays
#         time.sleep(30)  # Wait for 30 seconds to avoid excessive API requests

# if __name__ == "__main__":
#     main()

# Main function to simulate a live game
def main():
    game_id, home_team, away_team = get_live_game_id()
    
    if not game_id:
        print("No live game found.")
        return
    
    print(f"Simulating Live Game between {home_team} and {away_team}")
    print("=" * 60)

    interval = 5  # Define an interval for checking updates
    significant_actions = {'2pt', '3pt', 'freethrow', 'rebound', 'turnover'}  # Define key actions to focus on

    while True:
        pbp = playbyplay.PlayByPlay(game_id).get_dict()
        
        if 'game' in pbp and 'actions' in pbp['game']:
            plays = pbp['game']['actions']
            
            selected_plays = [play for play in plays[-interval:] if play['actionType'] in significant_actions]
            
            for play in selected_plays:
                prompt = format_prompt(play)
                prediction = get_gpt_prediction(prompt)
                
                # Display each play and the prediction in the specified format
                period = play['period']
                time_remaining = play['clock']
                description = play['description']
                score_home = play['scoreHome']
                score_away = play['scoreAway']
                team = play['teamTricode']
                player_name = play.get('playerName', 'Unknown Player')
                
                print(f"Quarter {period} - {time_remaining} Remaining:")
                print("Prediction:")
                print(f"- {player_name} from {team} just {description}.")
                print(f"- Current Score: {home_team} {score_home} - {away_team} {score_away}")
                print(f"- Possession: {team} {'has possession' if play.get('possession') else 'does not have possession'}")
                
                print("\nWin Probability:")
                print(prediction)
                print("\n" + "-" * 60 + "\n")
        
        time.sleep(30)  # Wait for 30 seconds before checking for new plays

if __name__ == "__main__":
    main()