# Importing
import re

# Reading Text File
text_file = open("input.txt","r")
lines = text_file.readlines()

# Initialising variables
data = {"Left": [], "Right": [], "Distance": []}

for line in lines:
    # Replacing sequential whitespace with a comma delimiter
    line = re.sub("\s+",",",line.strip())
    # Split the input string into left and right parts
    left, right = map(int, line.split(','))
    
    # Append to the respective columns
    data["Left"].append(left)
    data["Right"].append(right)

# Sort both the left and right columns to calculate the distance between them 
data["Left"].sort()
data["Right"].sort()

# Calculate the difference for every sorted pair
data["Distance"] = [abs(right - left) for left, right in zip(data["Left"], data["Right"])]

# Sum the total distance
totalDistance = sum(data["Distance"])
print(totalDistance)

text_file.close()
