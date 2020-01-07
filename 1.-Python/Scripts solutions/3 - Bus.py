# Variables
import statistics
stops = [(10, 0), (4, 1), (3, 5), (3, 4), (5, 1), (1, 5), (5, 8), (4, 6),
         (2, 3)]

# Q1
print("Number of stops:", len(stops))

# Q2
passengers = []
tracker = 0

"""
I have a doubt here, regarding that (tracker += + x - y)
Is the (+) x redundant? Could I just have tracker += x - y instead?
I tested and it gave me the same output back, but I was just wondering, because
if I didn't have += sign it would be tracker = tracker + x - y, right?
and if I took away the + sign, it would be tracker = tracker x - y?
Wouldn't there be an error there?
"""
for x, y in stops:
    tracker += + x - y
    passengers.append(tracker)

print("Number of passengers at each stop:", passengers)

# Q3
print("The maximum occupation of the bus is " + str(max(passengers)) + " passen\
gers.")

# Q4
"""
Don't know if we should try to round this up/down maybe?
To have a more realistic result. As we can't have 0.3 of a person.
"""
print("The average occupation is:", sum(passengers)/len(passengers))

print("The standard deviation is:", statistics.pstdev(passengers))
