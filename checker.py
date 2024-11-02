from nba_api.live.nba.endpoints import scoreboard
from datetime import datetime, timedelta, timezone

# Function to get upcoming games in the next few hours
def get_upcoming_games(hours_ahead=2):
    # Fetch today's games from the NBA scoreboard
    games = scoreboard.ScoreBoard().get_dict()['scoreboard']['games']
    
    # Filter for games scheduled to start within the next few hours
    upcoming_games = []
    now = datetime.now(timezone.utc)  # Current time in UTC (timezone-aware)
    
    for game in games:
        if game['gameStatus'] == 1:  # 1 means the game hasn't started yet
            # Parse the game start time (in UTC)
            game_time_str = game['gameTimeUTC']
            game_time = datetime.fromisoformat(game_time_str.replace('Z', '+00:00'))
            
            # Check if the game is scheduled to start within the specified time frame
            if now <= game_time <= now + timedelta(hours=hours_ahead):
                upcoming_games.append({
                    'gameId': game['gameId'],
                    'homeTeam': game['homeTeam']['teamName'],
                    'awayTeam': game['awayTeam']['teamName'],
                    'startTime': game_time
                })

    return upcoming_games

# Main function to check for upcoming games
def main():
    upcoming_games = get_upcoming_games(hours_ahead=2)  # Check for games in the next 2 hours

    if not upcoming_games:
        print("No upcoming games within the specified time frame.")
    else:
        print("Upcoming games within the next 2 hours:")
        for game in upcoming_games:
            print(f"{game['awayTeam']} vs {game['homeTeam']} - Scheduled Start: {game['startTime']} (UTC)")

if __name__ == "__main__":
    main()
