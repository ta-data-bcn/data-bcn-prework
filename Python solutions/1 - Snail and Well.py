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

# BONUS Q1
well_height = 125
advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
nightly_distance = 20
displacement = [x - 20 for x in advance_cm]
snail_position = 0
days = 0
print("Displacement:", displacement)

displacement_sum = ds = [sum(displacement[:i+1]) for i in range(len(displacement))]
print("Displacement sum:", ds)

for i in range(11):
    days += 1
    snail_position = ds[i]
    if snail_position > well_height:
        break

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
displacement = [x - 20 for x in advance_cm]
print("Max. displacement:", (max(displacement[:6])))
print("Min. displacement:", (min(displacement[:6])))

# BONUS Q3
total_progress = [x + 20 for x in advance_cm]
print("Average progress:", sum(total_progress)/len(total_progress))

# BONUS Q4
# I guess it is a sample and not population?
progress_with_night_slide = [x + 20 for x in advance_cm]
print("Standard deviation:", statistics.stdev(progress_with_night_slide))
