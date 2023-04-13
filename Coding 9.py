"""
Rose Bowl: The file, Rosebowl.txt Download Rosebowl.txt contains the names of the 
Rose Bowl winners (up through 2014) in the order the games were played. Write a program 
that displays the names of the teams that have won four or more Rose Bowls and the number 
of wins for each team. The teams should appear ordered by the number of wins. Use Exception
handling to open the file. For Extra credit update the file with the winners from 2014 - 2022.

This code opens the file "Rosebowl.txt" for reading and appending using a with statement. 
It first adds the winners from 2014 to 2022 to the end of the file by creating a list of winners and 
using the join method to concatenate them with newlines. It then moves the file pointer to the beginning 
of the file and loops through each line, counting the number of wins for each team using a dictionary. 
It filters the dictionary to include only teams with 4 or more wins and **Creative element** alphabetizes the resulting dictionary 
by team name. Finally, it prints the updated list of winners with the number of wins for each team.
The try block is used to catch any IOErrors that may occur when attempting to open the file. If an IOError 
occurs, the code prints an error message.

"""
# adding try block
try:
    # Open the file for reading and appending
    with open("Rosebowl.txt", "a+") as f:
        # Add the winners from 2014 to 2022
        winners = ["Michigan State", "Stanford", "Oregon", "TCU", "Iowa", "USC", "Oklahoma", "Georgia", "Ohio State"]
        f.write("\n")
        f.write("\n".join(winners))

        # Move the file pointer to the beginning of the file
        f.seek(0)

        # Create a dictionary to store the number of wins for each team
        wins = {}

        # Loop through each line of the file and count the wins for each team
        for line in f:
            team = line.strip()
            if team in wins:
                wins[team] += 1
            else:
                wins[team] = 1

        # Filter the dictionary to include only teams with 4 or more wins
        filtered_wins = {team: wins[team] for team in wins if wins[team] >= 4}

        # Alphabetize the dictionary by team name
        sorted_wins = dict(sorted(filtered_wins.items()))

        # Print the results
        for team, win_count in sorted_wins.items():
            print("Updated list of winners from 2014-2022")
            print(f"{team}: {win_count} wins")

except IOError:
    print("Error: Could not open file.")
