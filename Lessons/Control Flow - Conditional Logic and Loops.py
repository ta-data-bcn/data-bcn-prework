happy = True
print("Happy variable is set to ", happy)

print(5 + 5 == 10)
print('apple' != 'orange')
print(100 > 75)
print(93 < 80)
print(3 in [1, 2, 3, 4, 5])
print(3 not in [1, 2, 3, 4, 5])

# and(&) returns True if all conditions are true
# or (|) returns True if any of the conditions are true
# Don't forget to wrap each condition in ()
print((5 + 5 == 10) & ('apple' != 'orange'))
print((100 > 75) & (93 < 80))
print((100 > 75) | (93 < 80))
print((93 < 80) | (3 not in [1, 2, 3, 4, 5]))


# CONDITIONAL LOGIC
number = 10

if number < 10:
    print("Number is less than 10")
elif number > 10:
    print("Number is greater than 10")
elif number == 10:
    print("Number is exactly 10")
else:
    print("Number is probably not a number at all")

# A more complex example
commute = 30
rain = False
traffic = True

if (rain == True) | (traffic == True):
    if (rain == True) & (traffic == True):
        total_commute = commute + 15 + 20
    elif (rain == True) & (traffic == False):
        total_commute = commute + 15
    elif (rain == False) & (traffic == True):
        total_commute = commute + 20
else:
    total_commute = commute

print("Your total commute time is expected to be", total_commute, "minutes.")


# ITERATION

# FOR LOOPS
print(range(10))  # prints range(0, 10)
print(len(range(5, 15)))  # prints 10

for i in range(5, 15):  # remember that the for loop will not get the last numb
    print(i)

fruits = ['apple', 'orange', 'banana', 'grapes', 'pineapple']
# we can also loop through data structures

for fruit in fruits:
    print(fruit)

ages = {'Brian': 23, 'Amy': 22, 'Darlene': 47, 'Ralph': 32, 'Jordan': 28,
        'Stephanie': 35}

for name, age in ages.items():
    print(name, "is", age, "years old.")

num_list = [34, 12, 93, 783, 330, 896, 1, 55]

total = 0

for i in num_list:
    total += i
    print("Total is currently", total)

new_list = []

for i in range(1, 11):
    square = i**2
    new_list.append(square)

print(new_list)

# WHILE LOOPS
total_time = 60
minutes_elapsed = 0
wait = 15

print("Cake is in the oven.")

while minutes_elapsed < total_time:
    print("Cake is not done yet.")
    minutes_elapsed += wait

print("It's done. Let's eat cake!")
