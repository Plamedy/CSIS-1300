# Open the file for reading
infile = open("StatesANC.txt", "r")

# Initialize the counter
count = 0

# Loop to run the code again
while True:
    # Loop through each line of the file
    for line in infile:
        # Split the line into its parts
        state_parts = line.strip().split(",")
        state_name = state_parts[0]
        state_abbr = state_parts[1]
        state_nickname = state_parts[2]
        state_capital = state_parts[3]

        # Check if the state name and capital start with the same letter
        if state_name[0].lower() == state_capital[0].lower():
            print(f"{state_name} ({state_abbr}) - {state_capital}")
            count += 1

    # Close the file
    infile.close()

    # Print the count
    print(f"\n{count} state names and capitals start with the same letter.")

    # Ask the user if they want to run the code again
    response = input("Do you want to repeat this code? (y/n): ")
    if response.lower() == "y":
        # Open the file again for reading
        infile = open("StatesANC.txt", "r")
    else:
        break
