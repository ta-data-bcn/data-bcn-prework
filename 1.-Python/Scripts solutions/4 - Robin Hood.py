# import math

points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2),
          (4, 5), (3, 2), (5, 7),
          (-5, 7), (2, 2), (-4, 5), (0, -2),
          (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2),
          (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]


# Q1
"""
# Test 1 - I don't like this very much
temp = points[:]

for x in set(temp):
    temp.remove(x)

temp = list(set(temp))
print(temp)
"""

# Test 2 - I like this one a lot. Very simple and concise
dupes = set()

for i in points:
    if points.count(i) >= 2:
        dupes.add(i)

print("Coordinates of the points where an arrow hits another arrow:",
      list(dupes))


"""
# Test 3 - Interesting solution without sets. Preserves order
dups = []

for i in points:
    if dups.count(i) == 1:
        continue
    if points.count(i) >= 2:
        dups.append(i)

print(dups)
"""

# Q2
Q1 = 0
Q2 = 0
Q3 = 0
Q4 = 0

for x, y in points:
    if x > 0 and y > 0:
        Q1 += 1
    elif x < 0 and y > 0:
        Q2 += 1
    elif x < 0 and y < 0:
        Q3 += 1
    elif x > 0 and y < 0:
        Q4 += 1
    else:  # I guess this is redundant and not necessary?
        continue

print("Number of arrows in Q1:", Q1)
print("Number of arrows in Q2:", Q2)
print("Number of arrows in Q3:", Q3)
print("Number of arrows in Q4:", Q4)


# Q3
"""
# Test 1 - This concept seems slightly harder to understand than test 2
x = (0, -2)
y = (0, 0)
distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
print("Euclidean distance from x to y: ", distance)
"""

# Test 2
point_closest_to_the_center = pctc = []
distance_from_the_center = dfc = []

"""
By getting the minimum value of the 'distance_from_the_center' list we are able
to then use that value (2) to find the corresponding points whose
distance from the center equals that value
"""
for i in range(len(points)):
    euclidean_distace = (points[i][0] ** 2 + points[i][1] ** 2) ** 0.5
    dfc.append(euclidean_distace)

print("The minimum distance to the center is:", min(dfc))


for i in range(len(points)):
    euclidean_distace = (points[i][0] ** 2 + points[i][1] ** 2) ** 0.5
    if euclidean_distace == 2:
        pctc.append(points[i])

print("Points with the shortest distance to the center:", pctc)

# Q4
arrows_missed = am = 0

# I think that by making the euclidean_distace > 9 we achieve this radius of 9?
for i in range(len(points)):
    euclidean_distace = (points[i][0] ** 2 + points[i][1] ** 2) ** 0.5
    if euclidean_distace > 9:
        am += 1

print("Number of arrows that won't hit the target:", am)
