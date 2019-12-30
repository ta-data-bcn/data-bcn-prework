import statistics
well_height = 125
daily_distance = 30
nightly_distance = 20
snail_position = 0
days = 0

while snail_position < well_height:
    # print("The snail is not out yet.")
    days += 1
    snail_position += 10

print("The snail is finally out after", days, "days.")

# BONUS
well_height = [125]
advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
nightly_distance = 20
displacement = [x - 20 for x in advance_cm]
snail_position = [0]
days = 0
print(displacement)

while sum(snail_position) < sum(well_height):
    days += 1
    snail_position = displacement  # fix this

print("The snail is finally out after", days, "days.")


# TESTING FOR BONUS Q1
well_height = 125
advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
displacement = [x - 20 for x in advance_cm]
print(displacement)
snail_position = 0
days = 0

while snail_position < well_height:
    days += 1
    snail_position = 10 + 1 + 13 + 57 + 24 + 25
    # this is still not working - can't figure it out

print("The snail is finally out after", days, "days.")


# THIS ADDS THE NUMBER BEHIND IT AND RETURNS A NEW LIST
a = [1, 2, 3, 4]
for i in range(len(a)):
    a[i] += i
print(a)

# THIS FINALLY SUMS, STORES THE VALUE AND SUMS THE NEXT NUMBER
# IT GIVES ME THE RESULTS BACK IN AN INCREMENTAL LIST RATHER THAN A SIMPLE SUM
x = [1, 2, 3, 4]
y = [sum(x[:i+1]) for i in range(len(x))]
print(y)

# BONUS Q2
advance_cm2 = [30, 21, 33, 77, 44, 45]
displacement = [x - 20 for x in advance_cm2]
print(max(displacement))
print(min(displacement))

# BONUS Q3
advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
total_progress = [x + 20 for x in advance_cm]
print(sum(total_progress)/len(total_progress))

# BONUS Q4
advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
progress_with_night_slide = [x + 20 for x in advance_cm]
print(statistics.stdev(progress_with_night_slide))
