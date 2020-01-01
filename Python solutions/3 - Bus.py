# Variables
import statistics
stops = [(10, 0), (4, 1), (3, 5), (3, 4), (5, 1), (1, 5), (5, 8), (4, 6), (2, 3)]

# Q1
print("Number of stops:", len(stops))

# Q2
passengers = []
counter = 0

for x, y in stops:
    counter += + x - y
    passengers.append(counter)

print("Number of passengers at each stop:", passengers)

# Q3
print("The maximum occupation of the bus is " + str(max(passengers)) + " passengers.")

# Q4
# Don't know if we should try to round this up/down maybe?
print("The average occupation is:", max(passengers)/len(passengers))

print("The standard deviation is:", statistics.stdev(passengers))
