def read_results(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def calculate_score(results, guess):
    result_positions = {team: i for i, team in enumerate(results)}
    return sum((result_positions[team] - i) ** 2 for i, team in enumerate(guess))

def main():
    results = read_results('result.txt')
    result_set = set(results)
    
    with open('guess.txt', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            
            player = line.strip()
            if not player:
                break
            
            if not player.startswith('-'):
                print(f"Error: Player name '{player}' does not start with '-'. Stopping.")
                return
                
            guess = []
            for _ in range(20):
                team_line = f.readline()
                if not team_line:
                    print(f"Error reading the teams for Player: '{player}'. Stopping.")
                    break
                guess.append(team_line.strip())
            
            if len(guess) != 20:
                print(f"Error reading the teams for Player: '{player}'. Stopping.")
                break
                
            guess_set = set(guess)
            if guess_set != result_set:
                missing = result_set - guess_set
                extra = guess_set - result_set
                wrong_teams = list(missing) + list(extra)
                print(f"{player}: Invalid guess - wrong teams: {', '.join(wrong_teams)}")
                continue
            
            score = calculate_score(results, guess)
            print(f"{player}: {score}")

if __name__ == "__main__":
    main()