# Importing
import re

# Reading Text File
text_file = open("input.txt","r")
lines = text_file.readlines()

# Initialising variables
data = {"Left": [], "Right": [], "Similarity": []}

for line in lines:
    # Replacing sequential whitespace with a comma delimiter
    line = re.sub("\s+",",",line.strip())
    # Split the input string into left and right parts
    left, right = map(int, line.split(','))
    
    # Append to the respective columns
    data["Left"].append(left)
    data["Right"].append(right)



# Calculate the similarity of each left element and the number of appearances in the right column
data["Similarity"] = [left * data["Right"].count(left) for left in data["Left"]]

# Sum the total distance
Similarity = sum(data["Similarity"])
print(Similarity)

text_file.close()
