print(len("automobile"))

word = "automobile"

# In python, counting starts with 0 and not 1
# We can use the indexes 0, 1, 2, etc. to reference something in that position
print(word[0])
print(word[-1])
# If we use a negative index we start from the end


"""
Everything to the right of the : doesn't get included when slicing
That means we go up to, but not including, index 4, for instance
"""
print(word[:4])
print(word[4:])
print(word[3:8])


# LISTS

lst = ["The", "man", "in", "the", "blue", "suit"]

print(lst[0])
print(lst[1])
print(lst[-1])
print(lst[2:4])

lst.append("jacket")
print(lst)

lst.remove("suit")
print(lst)

lst2 = ["and", "the", "green", "trousers"]

comb_list = lst + lst2
print(comb_list)

# NESTED LISTS - Lists that also contain other lists as their elements

nested = [["A", "man"], ["a", "plan"], ["a", "canal"], ["Panama", "!"]]

print(nested[0])  # prints ["A", "man"]
print(nested[0][1])  # prints "man"
print(nested[-1][0])  # prints "Panama"

# We can also do mathematical operations with numeric lists

num_list = [34, 12, 93, 783, 330, 896, 1, 55]

# Sum
print(sum(num_list))

# Mean
print(sum(num_list)/len(num_list))

# Minimum
print(min(num_list))

# Maximum
print(max(num_list))

# Sort ascending
num_list.sort()
print(num_list)

# Sort descending
num_list.sort(reverse=True)
print(num_list)

# Reversing
num_list.reverse()
print(num_list)


# DICTIONARIES
"""
Dictionary elements are key-value pairs where keys and values are mapped to
each other by colons, split from other key-value pairs via commas,
and the entire collection of them is wrapped in curly braces
"""

ages = {"Brian": 23, "Amy": 22, "Darlene": 47, "Ralph": 32, "Jordan": 28,
        "Stephanie": 35}

# With dictionaries, we retrieve a value by referencing its key
print(ages["Brian"])  # prints the value 23
print(ages["Stephanie"])  # prints the value 35

"""
We can retrieve all the keys or values in a dictionary
with the keys() or values() method
"""
print(ages.keys())
print(ages.values())

# Adding items to a dictionary
ages["Vanessa"] = 30
print(ages)

# Deleting items from a dictionary
del ages["Vanessa"]
print(ages)


# TUPLES
"""
They are very similar to lists, but the key difference
is that they are IMMUTABLE and are enclosed in ()
"""
a = [1, 2, 3, 4, 5]
b = (1, 2, 3, 4, 5)

a.append(6)
print(a)

# b.append(6)
"""
That would give us an error, as a tuple does not have
the same attributes as a list, hence its immutability.
We cannot append(), remove() or sort() a tuple
"""

# We can, however, convert a list to a tuple and vice-versa
tuple(a)
print(a)

list(b)
print(b)
# THIS DOESN'T SEEM TO BE WORKING!


# SETS
"""
They are a useful data structure that allows us to
remove duplicates in a list or tuple.
"""
dupe_list = [1, 2, 2, 3, 3, 4, 4, 5, 5]
uniques = set(dupe_list)
print(uniques)
