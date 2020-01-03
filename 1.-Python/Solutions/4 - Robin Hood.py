points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2),
          (4, 5), (3, 2), (5, 7),
          (-5, 7), (2, 2), (-4, 5), (0, -2),
          (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2),
          (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]


# Q1
# Test 1 - I don't like this very much
temp = points[:]

for x in set(temp):
    temp.remove(x)

temp = list(set(temp))
print(temp)


# Test 2 - I like this one a lot. Very simple and concise
dupes = set()

for i in points:
    if points.count(i) >= 2:
        dupes.add(i)

print("Coordinates of the points where an arrow hits another arrow:",
      list(dupes))


# Test 3 - Interesting solution without sets. Preserves order
dups = []

for i in points:
    if dups.count(i) == 1:
        continue
    if points.count(i) >= 2:
        dups.append(i)

print(dups)

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
