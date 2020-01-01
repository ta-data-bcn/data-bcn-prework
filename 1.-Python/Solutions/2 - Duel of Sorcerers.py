import statistics
# import random
gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]
spells = 0

gandalf_wins = 0
saruman_wins = 0

for i in range(10):
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
# print("The final winner is:", final_winner)

if gandalf_wins > saruman_wins:
    print("Gandalf wins")
elif saruman_wins > gandalf_wins:
    print("Saruman wins")
else:
    print("Tie")

# THIS IS HOW IT SHOULD ACTUALLY BE? (don't forget the spells)
# for i in range(10):
#    if gandalf[random.choice(gandalf)] > saruman[random.choice(saruman)]:
#        gandalf_wins += 1

#    if saruman[random.choice(saruman)] > gandalf[random.choice(gandalf)]:
#        saruman_wins += 1


# BONUS
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

gandalf_wins = 0
saruman_wins = 0

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

# BONUS Q4 - SPELL CLASH
# gp = gandalf_power[random.choice(gandalf_power)]
# sp = saruman_power[random.choice(saruman_power)]
print("Spell clash starting now! May the best sorcerer win!")

for i in range(10):
    if gandalf_power[i] > saruman_power[i] and gandalf_power[i+1] > saruman_power[i+1] and gandalf_power[i+2] > saruman_power[i+2]:
        gandalf_wins += 1

    elif gandalf_power[i] < saruman_power[i] and gandalf_power[i+1] < saruman_power[i+1] and gandalf_power[i+2] < saruman_power[i+2]:
        saruman_wins += 1

    if gandalf_wins > 0 or saruman_wins > 0:
        break

if gandalf_wins > saruman_wins:
    print("Winner: Gandalf")
elif gandalf_wins < saruman_wins:
    print("Winner: Saruman")
else:
    print("Tie")

# BONUS Q5
print("Calculating the average spell power of each sorcerer. Please wait.")

print("Average spell power of Gandalf:", sum(gandalf_power)/len(gandalf_power))

print("Average spell power of Saruman:", sum(saruman_power)/len(saruman_power))

# BONUS Q6
# Doubts about using population or sample formula
# Maybe it is pop since we only have 1 Gandalf and Saruman?
print("Gandalf's spell power standard deviation:", statistics.pstdev(gandalf_power))

print("Saruman's spell power standard deviation:", statistics.pstdev(saruman_power))
