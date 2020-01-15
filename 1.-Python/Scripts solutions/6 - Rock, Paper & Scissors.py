from random import choice

# Q2
gestures = ["rock", "paper", "scissors"]

# Q3
n_rounds = int(input("Please input an odd number of rounds to play: "))

# Q4
rounds_to_win = int((n_rounds / 2) + 1)

# Q5
cpu_score = 0
player_score = 0


# Q6


def computer_gesture():
    return choice(gestures)


comp_choice = computer_gesture()


# Q7


def player_gesture():

    while True:
        gesture = input("Please choose between 'rock', \
        'paper' or 'scissors': ")

        if gesture.lower() == "rock" or gesture.lower() == "paper" or gesture.lower() == "scissors":
            break

        else:
            continue

    return gesture


player_choice = player_gesture()


# Q8


def round_winner(comp_choice, player_choice):

    if comp_choice == "rock" and player_choice == "paper":
        return 2

    elif comp_choice == "rock" and player_choice == "scissors":
        return 1

    elif comp_choice == "paper" and player_choice == "rock":
        return 1

    elif comp_choice == "paper" and player_choice == "scissors":
        return 2

    elif comp_choice == "scissors" and player_choice == "rock":
        return 2

    elif comp_choice == "scissors" and player_choice == "paper":
        return 1

    else:
        return 0


who_won_round = round_winner(comp_choice, player_choice)


# Q9


def results_printer():

    print(comp_choice)
    print(player_choice)

    if who_won_round == 1:
        print("Computer won.")
        global cpu_score
        cpu_score += 1

    if who_won_round == 2:
        print("Player won.")
        global player_score
        player_score += 1

    if who_won_round == 0:
        print("Tie.")
        cpu_score += 0
        player_score += 0


results_printer()


# Q10

round_counter = 0

while (cpu_score != rounds_to_win or player_score != rounds_to_win) and round_counter != n_rounds:

    player_choice = player_gesture()
    comp_choice = computer_gesture()
    results_printer()
    round_counter += 1
    print("Number of rounds played:", round_counter)


# Q11

if cpu_score > player_score:
    print("The final winner is: The Computer")
else:
    print("The final winner is: The Player")
