import random

print("PIG dice game")


def roll():
    rolling = random.randint(1, 6)
    return rolling


while True:
    players = input("Enter the number of players(2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Players must be in range 2-4")
    else:
        print("Put valid numbers please")
max_score = 100
players_score = [0 for i in range(players)]

while max(players_score) < max_score:
    for player_id in range(players):
        print(f"\nPlayer number {player_id + 1} turn has started")
        print(f"Your total score is {players_score[player_id]}")
        current_score = 0

        while True:
            want_to_roll = input("Do you want to roll the dice?\n")
            if want_to_roll[0] == 'y'.lower():
                dice = roll()
                if dice > 1:
                    print(f"You rolled {dice}")
                    current_score += dice
                    print(f"Your current score is: {current_score}")
                elif dice == 1:
                    print("You rolled 1. End of turn")
                    current_score = 0
                    break
            else:
                break
        players_score[player_id] += current_score
        print(f"Your total score is: {players_score[player_id]}")

max_score = max(players_score)
winner = players_score.index(max_score)
print(f"Player {winner + 1} is the winner with {max_score}")
