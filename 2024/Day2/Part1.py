# Importing
import re
import numpy as np

#Function to check to see if a given report is healthy
def healthyReport(report):
    i = 0
    healthy = True
    Direction = 0

    #checking each element in the report array
    for level in report:
        if i > 0: 
            if level > previousLevel:
                Direction = 1 #"1" is considered increasing 
            elif level < previousLevel:
                Direction = -1 #"-1" is considered decreasing 
            else:
                healthy = False #unhealthy if there is no movement
        
            if i>1 and Direction != previousDirection: #unhealthy if there is a direction change
                healthy = False
                
            if abs(previousLevel-level) < 1 or abs(previousLevel-level) > 3:
                healthy = False #unhealthy if there is too large a change
            
            if not(healthy):
                healthy = dampener(report,i) # call the dampener function for part 2
                return healthy
        
        previousDirection = Direction
        previousLevel = level
        i+=1
    return healthy

# Function to see if an outlier value was causing an unreasonable unhealthy condition
# Function to be called on a report that has been flagged as unhealthy
# Inputs of the unhealthy report and the index at which the report faulted
def dampener(report, i):
    # 4 viable positions under which the fault could occur
    test1 = report.copy()
    test2 = report.copy()
    test3 = report.copy()
    test4 = report.copy()
    
    # Setting up the 4 different test cases
    tests = [test1, test2, test3, test4]
    test1.pop(i-2)
    test2.pop(i-1)
    test3.pop(i)
    if i+1 < len(report):
        test4.pop(i+1)

    # Test the 4 different cases
    for test in tests:
        i=0
        healthy = True
        Direction = 0
        for level in test:
            if i > 0: 
                if level > previousLevel:
                    Direction = 1 #"1" is considered increasing 
                elif level < previousLevel:
                    Direction = -1 #"-1" is considered decreasing 
                else:
                    healthy = False #unhealthy if there is no movement
            
                if i>1 and Direction != previousDirection: #unhealthy if there is a direction change
                    healthy = False
                    
                if abs(previousLevel-level) < 1 or abs(previousLevel-level) > 3:
                    healthy = False #unhealthy if there is too large a change
        
            previousDirection = Direction
            previousLevel = level
            i+=1
        if healthy:
            return healthy # Return healthy as soon as a healthy test is found
        

# Setup
numHealthy = 0

# Reading Text File
text_file = open("input.txt","r")
lines = text_file.readlines()

# Mapping the text file into an array of Dints
array = [list(map(int,line.split())) for line in lines]
for report in array:
    # Checking and counting the number of healthy reports
    if healthyReport(report):
        numHealthy += 1

print(numHealthy)