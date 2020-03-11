import numpy as np

player_A_strategy = [1/3, 1/3, 1/3]
player_A_actions = ["paper", "scissors", "rock"]
player_B_strategy = [0/3, 2/3, 1/3]
player_B_actions = ["paper", "scissors", "rock"]

player_A_victory = [("paper", "rock"),
                    ("scissors", "paper"),
                    ("rock", "scissors")]


def play(player_A_strategy, player_B_strategy):
    # draw action a
    action_a = "paper"
    action_b = "rock"
    print("\nA : "+action_a+", B : "+action_b)

    if action_a == action_b:
        result = 0
        print("draw")
    else:
        if (action_a, action_b) in player_A_victory:
            print("player A wins")
            result = 1
        else:
            result = -1
            print("player B wins")
    return result


number_of_games = 10000
played_games = 0
player_A_victories = 0
player_A_sum = 0
for game in range(number_of_games):
    result = play(player_A_strategy, player_B_strategy)
    played_games += 1
    player_A_sum += result
    average = player_A_sum
    print(f"expectation of return after {played_games} games : {average}")
    print(f"percentage of victory {100*player_A_victories/played_games}")
