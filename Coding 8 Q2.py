# Open the file for reading
infile = open("StatesANC.txt", "r")

# Create a dictionary to store state information
states = {}

# Loop through each line of the file and store state information in dictionary
for line in infile:
    # Split the line into name, abbreviation, nickname, and capital
    state_info = line.strip().split(',')
    
    # Store state information in dictionary
    name = state_info[0]
    abbreviation = state_info[1]
    nickname = state_info[2]
    capital = state_info[3]
    states[name] = (abbreviation, nickname, capital)

# Close the file
infile.close()

# Repeat until the user chooses to quit
while True:
    # Ask the user for a state name
    state = input("Enter the name of a state (or 'quit' to exit): ")
    
    # Check if the user wants to quit
    if state.lower() == 'quit':
        break
    
    # Look up state information in dictionary
    if state in states:
        abbreviation, nickname, capital = states[state]
        print("Abbreviation:", abbreviation)
        print("Nickname:", nickname)
        print("Capital:", capital)
    else:
        print("State not found in file.")
    
    # Ask the user if they want to run the code again
    run_again = input("Do you want to run the code again? (y/n): ")
    if run_again.lower() != 'y':
        break
