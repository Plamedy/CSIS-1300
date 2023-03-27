"""Alphabetical Order: The following words have three consecutive letters that are also consecutive letters
   in the alphabet: THIRSTY, NOPE, AFGHANISTAN, STUDENT. Write a program that accepts a word as input and 
   determines whether or not it has three consecutive letters that are consecutive letters in the alphabet. 
   The program should use a ­Boolean-​­valued function named isTripleConsecutive that accepts an entire word 
   as input. Hint: Use the word function.
"""
def isTripleConsecutive(word):
    for i in range(len(word) - 2):
        if ord(word[i]) == ord(word[i+1]) - 1 and ord(word[i]) == ord(word[i+2]) - 2:
            return True
    return False

word = input("Enter a word: ")
if isTripleConsecutive(word):
    print("The word has three consecutive letters that are consecutive letters in the alphabet.")
else:
    print("The word does not have three consecutive letters that are consecutive letters in the alphabet.")