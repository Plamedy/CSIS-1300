"""
The file Numbers.txt  Download Numbers.txtcontains the integers 6, 9, 2, 3, 6, 4 with each integer
on a separate line. Write a program that uses the file to carry out the task without using lists.
34. Display the number of numbers in the file Numbers.txt. 
35. Display the largest number in the file Numbers.txt.
36. Display the smallest number in the file Numbers.txt
"""
# Allows "random" into code 
import random

# Open the file for reading
infile = open("Numbers.txt", "r")

# Initialize variables
count = 0
max_num = float('-inf')
min_num = float('inf')

# Loop through each line of the file
for line in infile:
    # Convert the line to an integer
    num = int(line.strip())
    
    # Update count, max_num, and min_num
    count += 1
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

# Close the file
infile.close()

# Display the results
print("The number of integers in the file is:", count)
print("The largest number in the file is:", max_num)
print("The smallest number in the file is:", min_num)

# Get a random number from the file
rand_num = random.randint(1, count)
infile = open("Numbers.txt", "r")
for i in range(rand_num):
    line = infile.readline().strip()
    if i == rand_num - 1:
        print("A random number from the file is:", line)
        break

# Close the file
infile.close()