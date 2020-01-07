import statistics

well_height = 125
daily_distance = 30
nightly_distance = 20
snail_position = 0
days = 0

while snail_position < well_height:
    days += 1
    snail_position += daily_distance
    if snail_position >= well_height:
        break
    else:
        snail_position -= nightly_distance

print("The snail is finally out after", days, "days.")


# BONUS

# BONUS Q1
well_height = 125
advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
nightly_distance = 20
displacement = [x - 20 for x in advance_cm]
snail_position = 0
days = 0
print("Displacement:", displacement)

"""
Well, the snail sits at the 125cm mark on the 5th day.
One would think it would simply crawl out of the well.
However, the exercise explicitly says it has to surpass 125cm to escape.
So, it will still need to spend another night at the well, only to escape
the morning after.
Anyhow, this can be fixed by simply changing the sign in the if clause to ">="
Also, I decided to keep my foor loop so I wouldn't have to rewrite much
turning it into another while loop.
"""
for i in range(len(advance_cm)):
    days += 1
    snail_position += advance_cm[i]
    if snail_position > well_height:
        break
    else:
        snail_position -= nightly_distance

print("The snail is finally out after", days, "days.")


"""
# THIS ADDS THE NUMBER BEHIND IT AND RETURNS A NEW LIST
a = [1, 2, 3, 4]
for i in range(len(a)):
    a[i] += i
print(a)

# THIS FINALLY SUMS, STORES THE VALUE AND SUMS THE NEXT NUMBER
# IT GIVES ME THE RESULTS BACK IN AN INCREMENTAL LIST RATHER THAN A SIMPLE SUM
Turns out I didn't need this afterall, with the rework I've done in Bonus Q1
x = [1, 2, 3, 4]
y = [sum(x[:i+1]) for i in range(len(x))]
print(y)
"""

# BONUS Q2
print("Max. displacement:", (max(displacement[:6])))
print("Min. displacement:", (min(displacement[:6])))

# BONUS Q3
print("Average progress:", sum(displacement)/len(displacement))

# BONUS Q4
print("Standard deviation:", statistics.pstdev(displacement))
