"""Alphabetical Order: The following words have three consecutive letters that are also consecutive letters
   in the alphabet: THIRSTY, NOPE, AFGHANISTAN, STUDENT. Write a program that accepts a word as input and 
   determines whether or not it has three consecutive letters that are consecutive letters in the alphabet. 
   The program should use a Boolean valued function named isTripleConsecutive that accepts an entire word 
   as input. Hint: Use the word function.
"""
def isTripleConsecutive(word): # function named isTripleConsecutive that accepts an entire word as an input
    for i in range(len(word) - 2): # for loop that iterates over the characters in the word, comparing each character with the two next ones
        if ord(word[i]) == ord(word[i+1]) - 1 and ord(word[i]) == ord(word[i+2]) - 2: #ord function used  to convert each character to its ASCII code
            return True # returns True if the word has three consecutive letters that are consecutive letters in the alphabet
    return False # returns Flase if not

word = input("Enter a word: ") 
if isTripleConsecutive(word):
    print("The word has three consecutive letters that are consecutive letters in the alphabet.") # Prints if ...
else:
    print("The word does not have three consecutive letters that are consecutive letters in the alphabet.") # Prints if ...

 choice = input("Do you want to check another word? (Y/N)").lower() # Asks user if they'd like to run the code again
    if choice == 'n': # If the user types "n" when prompted, the code ends, while tying anything else will result in the code running again.
        break