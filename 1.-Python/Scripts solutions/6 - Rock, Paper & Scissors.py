from random import choice

# Q2
gestures = ["rock", "paper", "scissors"]

# Q3
n_rounds = 0

# Q4
rounds_to_win = 0

# Q5
cpu_score = 0
player_score = 0

# Q6


def computer_gesture():
    print(choice(gestures))


computer_gesture()

# Q7


def player_gesture():

    while True:
        gesture = str(input("Please choose between 'rock', 'paper' \
        or 'scissors': "))

        if gesture.lower() == "rock" or gesture.lower() == "paper" or \
                gesture.lower() == "scissors":
            break

        else:
            continue

    print(gesture)  # Is this necessary?


player_gesture()

# Q8

# Can't get it to work. Tried many different ways.


def round_winner():
    if computer_gesture() == "rock" and player_gesture() == "paper":
        print("test 1")
    elif computer_gesture() == "paper" and player_gesture() == "paper":
        print("test 2")
    elif computer_gesture() == "scissors" and player_gesture() == "paper":
        print("test 3")
    else:
        print("still not working lol")


round_winner()
