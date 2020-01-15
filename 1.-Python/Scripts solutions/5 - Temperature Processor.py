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
# Test 1 - Also works
"""
test = []

for i in range(len(temperatures_C)):
    if temperatures_C[i] > 70:
        test.append(i)
print("Test list of hours with temps > 70°C:", test)
"""

# Test 2
hours_temps_greater_70 = ht70 = []

for i, x in enumerate(temperatures_C):
    if x > 70:
        ht70.append(i)

print("List of hours where the temperature is > 70°C:", ht70)


# Q2
# Interesting way to get the index of a value in temperatures_C list.
# print([i for i, e in enumerate(temperatures_C) if e == 76])

for i in range(len(ht70)):

    if (ht70[1] - ht70[0] == 1
        and ht70[2] - ht70[1] == 1
        and ht70[3] - ht70[2] == 1
        and ht70[4] - ht70[3] == 1
            and ht70[5] - ht70[4] == 1):
        consecutive_hours = "Yes"

    else:
        consecutive_hours = "No"

if "Yes" in consecutive_hours:
    print("The list has more than 4 consecutive hours.")
else:
    print("The list doesn't have more than 4 consecutive hours.")

"""
# I also thought about this. Is this better? Or is it incorrect?
# I think it kinda makes sense?

for i in range(len(ht70)):

    if (ht70[i]+1 - ht70[i]) == 1:
        consecutive_hours = "Yes"

    else:
        consecutive_hours = "No"

if "Yes" in consecutive_hours:
    print("The list has more than 4 consecutive hours.")
else:
    print("The list doesn't have more than 4 consecutive hours.")
"""

# Q3
if consecutive_hours == "Yes" or max(temperatures_C) > 80 or avg_temp > 65:
    print("The cooling system needs to be changed.")

else:
    print("The cooling system does not need to be changed.")


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

print("The standard deviation in Fahrenheit is 1.8* higher than the \
standard deviation in Celsius. We can verify that by dividing the SD in F by \
the SD in C, which will gives us 1.8 as a result.")

print("Result of dividing the SD in F by the SD in C:",
      statistics.pstdev(temps_in_F)/statistics.pstdev(temperatures_C))
