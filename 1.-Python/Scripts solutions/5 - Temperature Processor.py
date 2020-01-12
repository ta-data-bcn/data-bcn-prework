import statistics

temperatures_C = [33, 66, 65, 0, 59, 60, 62, 64, 70, 76,
                  80, 81, 80, 83, 90, 79, 61, 53, 50, 49, 53, 48, 45, 39]

# Q1
min_temp = min(temperatures_C)
print("The minimum temperature of the day is: " + str(min_temp) + "°C")


# Q2
max_temp = max(temperatures_C)
print("The maximum temperature of the day is: " + str(max_temp) + "°C")


# Q3
temp_greater_than_or_equal_to_70 = tp70 = []

for i in temperatures_C:
    if i >= 70:
        tp70.append(i)

# I wonder if it's ok to sort it, or if I should even just set it.
tp70.sort()
print("List of temperatures >= 70°C:", tp70)


# Q4
avg_temp = sum(temperatures_C)/len(temperatures_C)
print("The average temperature of the day is: " + str(avg_temp) + "°C")


# Q5
est_temp_3am = round((temperatures_C[2] + temperatures_C[4]) / 2)

print("The estimated temperature at 3am would be \
the mean of the temperatures at 2am and 4am: " + str(est_temp_3am) + "°C")

temperatures_C[3] = est_temp_3am

print("Updated list of temperatures with the \
missing estimated 3am value:", temperatures_C)


# Q6
temps_in_F = []

for i in range(len(temperatures_C)):
    temps_in_F.append(round((1.8 * temperatures_C[i]) + 32))

print("List of temperatures in Fahrenheit:", temps_in_F)


# Q7
if len(tp70) >= 4 or max(temperatures_C) > 80 or avg_temp > 65:
    print("The cooling system needs to be changed.")
else:
    print("The cooling system does not need to be changed.")


# BONUS

# Q1
# Test 1
"""
hours_temps_greater_70 = ht70 = []

for i in range(len(temperatures_C)):
    if temperatures_C[i] > 70:
        ht70.append(i)
print("Hours >70C with correct 'index':", ht70)
"""

# Test 2
hours_temps_greater_70 = ht70 = []

for i, x in enumerate(temperatures_C):
    if x > 70:
        ht70.append(i)

print("List of hours where the temperature is > 70°C:", ht70)

# Q2
print([i for i, e in enumerate(temperatures_C) if e == 76])


# Q4
print("Average value of the Celsius \
list:", sum(temperatures_C)/len(temperatures_C))

print("Average value of the Fahrenheit list:", sum(temps_in_F)/len(temps_in_F))

print("The relation between both average values is that the average \
in Fahrenheit is equal to 1.8 * the average value in Celsius + 32.")

# Q5
print("Standard deviation of the temperature list \
in Celsius:", statistics.pstdev(temperatures_C))

print("Standard deviation of the temperature list in \
Fahrenheit:", statistics.pstdev(temps_in_F))

print(statistics.pstdev(temps_in_F)/statistics.pstdev(temperatures_C))
