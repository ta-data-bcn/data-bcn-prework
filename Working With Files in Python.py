import os
print(os.getcwd())

folder_name = "new_folder"
if os.path.exists(folder_name) == False:
    os.makedirs(folder_name)

# This will create the "example.txt" file and write to it
with open("example.txt", "w") as f:
    f.write("Hello World! \n")
    f.write("How are you? \n")
    f.write("I'm fine.")

with open("example.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line)

data = []

with open("/Users/mattymrc/Desktop/Ironhack/data-bcn-prework/weight_height.csv", "r") as f:
    lines = f.readlines()
    for line in lines:
        data.append(line.split()[0].split(","))

print(data)

heights = []

for person in data[1:]:
    height = int(person[2])
    heights.append(height)

avg_height = sum(heights)/len(heights)
print(avg_height)

male_heights = []
female_heights = []

for person in data[1:]:
    height = int(person[2])  # Why not start with "1"?
    if person[0] == 'M':
        male_heights.append(height)
    elif person[0] == 'F':
        female_heights.append(height)

avg_male_height = sum(male_heights)/len(male_heights)
avg_female_height = sum(female_heights)/len(female_heights)

print("Avg male height:", avg_male_height)
print("Avg female height:", avg_female_height)
