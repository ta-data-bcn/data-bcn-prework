import statistics as stat
# import random

gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]
spells = 0

gandalf_wins = 0
saruman_wins = 0
# ties = 0

for i in range(len(gandalf)):
    if gandalf[i] > saruman[i]:
        gandalf_wins += 1
        spells += 2

    elif saruman[i] > gandalf[i]:
        saruman_wins += 1
        spells += 2

print("Wins for Gandalf:", gandalf_wins)
print("Wins for Saruman:", saruman_wins)
# print("Number of ties:", ties)
print("A total of", str(spells) + " spells have been cast.")

if gandalf_wins > saruman_wins:
    print("Gandalf wins.")
elif saruman_wins > gandalf_wins:
    print("Saruman wins.")
else:
    print("Tie.")

"""
# IS THIS HOW IT SHOULD ACTUALLY BE?
for i in range(len(gandalf)):
    if gandalf[random.choice(gandalf)] > saruman[random.choice(saruman)]:
        gandalf_wins += 1
        spells += 2

    if saruman[random.choice(saruman)] > gandalf[random.choice(gandalf)]:
        saruman_wins += 1
        spells += 2
"""

# BONUS

# Q1
power = {
    'Fireball': 50,
    'Lightning bolt': 40,
    'Magic arrow': 10,
    'Black Tentacles': 25,
    'Contagion': 45
}

gandalf = ['Fireball', 'Lightning bolt', 'Lightning bolt',
           'Magic arrow', 'Fireball', 'Magic arrow',
           'Lightning bolt', 'Fireball', 'Fireball',
           'Fireball']

saruman = ['Contagion', 'Contagion', 'Black Tentacles',
           'Fireball', 'Black Tentacles', 'Lightning bolt',
           'Magic arrow', 'Contagion', 'Magic arrow',
           'Magic arrow']

# Q2
gandalf_wins = 0
saruman_wins = 0

# Q3
gandalf_power = []
saruman_power = []

for spell in gandalf:
    if spell in power.keys():
        gandalf_power.append(power[spell])

print("Gandalf's power list:", gandalf_power)

for spell in saruman:
    if spell in power.keys():
        saruman_power.append(power[spell])

print("Saruman's power list:", saruman_power)


# Q4 - SPELL CLASH
# gp = gandalf_power[random.choice(gandalf_power)]
# sp = saruman_power[random.choice(saruman_power)]
print("Spell clash starting now! May the best sorcerer win!")

for i in range(len(gandalf_power)):
    if gandalf_power[i] > saruman_power[i]:
        gandalf_wins += 1
        saruman_wins = 0

    elif gandalf_power[i] < saruman_power[i]:
        saruman_wins += 1
        gandalf_wins = 0

    else:
        gandalf_wins = gandalf_wins
        saruman_wins = saruman_wins

    if gandalf_wins == 3 or saruman_wins == 3:
        break

if gandalf_wins > saruman_wins:
    print("Winner: Gandalf")
elif gandalf_wins < saruman_wins:
    print("Winner: Saruman")
else:
    print("Tie")


# BONUS Q5
"""
It would be cool if we could maybe have a delay for the 2nd and 3rd
print commands, that way the 1st print command makes more sense.
But I guess that wouldn't be able to happen in a text editor,
perhaps in a repl environment?
"""
print("Calculating the average spell power of each sorcerer. Please wait.")

print("Average spell power of Gandalf:", sum(gandalf_power)/len(gandalf_power))

print("Average spell power of Saruman:", sum(saruman_power)/len(saruman_power))


# BONUS Q6
"""
I had doubts whether it was a sample or population, but I
decided to use population here as we only have 1 Gandalf and 1 Saruman.
In the snail challenge I used sample as I thought we were only analyzing
the data of 1 snail and not the entire snail population.
That was my thought process.
"""
print("Gandalf's spell power standard deviation:", stat.pstdev(gandalf_power))

print("Saruman's spell power standard deviation:", stat.pstdev(saruman_power))
