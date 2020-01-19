from random import choice


# Q2
gestures = ["rock", "paper", "scissors"]


# Q3

def numb_rounds():

    while True:
        n_rounds = input("Please input an odd number of rounds to play: ")

        try:

            if int(n_rounds) % 2 != 0:
                print("Got it.")
                break

            elif int(n_rounds) % 2 == 0:
                print("This is an even number.")

        except ValueError:
            if isinstance(n_rounds, str) is True:
                print("This is not a number.")

    return int(n_rounds)


n_rounds = numb_rounds()


# Q4
rounds_to_win = int((n_rounds / 2) + 1)

print("The player needs to win " + str(rounds_to_win) + " rounds to win \
the game.")


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

def results_printer(who_won_round, comp_choice, player_choice):

    print(comp_choice)
    print(player_choice)

    if who_won_round == 1:
        print("Computer won.")
        global cpu_score
        cpu_score += 1
        return cpu_score

    elif who_won_round == 2:
        print("Player won.")
        global player_score
        player_score += 1
        return player_score

    elif who_won_round == 0:
        print("Tie.")
        cpu_score += 0
        player_score += 0
        return cpu_score and player_score


results = results_printer(who_won_round, comp_choice, player_choice)


# Q10

# I think now it is working 100% properly!!!

def game():

    round_counter = 0
    """
    Had to set the cpu and player scores back to 0 here,
    otherwise they would assume previous values from the first time
    I had to run everything
    """
    global cpu_score
    cpu_score = 0
    global player_score
    player_score = 0

    while (cpu_score != rounds_to_win or player_score != rounds_to_win) and round_counter != n_rounds:

        comp_choice = computer_gesture()
        player_choice = player_gesture()
        who_won_round = round_winner(comp_choice, player_choice)
        results = results_printer(who_won_round, comp_choice, player_choice)
        round_counter += 1
        print("Number of rounds played:", round_counter)


game()


# Q11
"""
Added these print statements to help me check whether or not
previous wins were being computed, and they were.
So that's why I set the global scores back to 0 in the 'game' function above
"""
print("Computer score:", cpu_score)
print("Player score:", player_score)

if cpu_score > player_score:
    print("The final winner is: The Computer")

elif cpu_score == player_score:  # added possibility of game ending in a tie.
    print("The game ended in a tie.")

else:
    print("The final winner is: The Player")
