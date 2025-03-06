import csv

# Open the election data CSV file
with open("/Users/nguyengiang/Downloads/Starter_Code-4/PyPoll/Resources/election_data.csv","r") as csv_file:

    # Read the CSV file using DictReader (treats each row as a dictionary with column headers as keys)
    election_csv = csv.DictReader(csv_file)

    #Initialize variables
    num_vote = 0 # Total number of votes
    candidate_list = [] # List to store unique candidate names
    candidate_vote = {} # Dictionary to store the vote count for each candidate

    # Loop through each row in the dataset
    for row in election_csv:
        num_vote += 1 # Increment total vote count
        candidate = row['Candidate'] # Extract candidate's name from the row

        # If candidate is not in the list add them
        if candidate not in candidate_list:
            candidate_list.append(candidate)

        # If candidate is not in the vote dictionary, initialize their count to 1
        if candidate not in candidate_vote:
            candidate_vote[candidate] = 1
        else:
            # Otherwise, increment their vote count
            candidate_vote[candidate] +=1

    # Print election results
    print(f'Election Results')
    print("-------------------------")
    print(f'Total Vote: ' + str(num_vote))
    print("-------------------------")

    # Loop through each candidate to calculate and print their vote percentage and total votes
    for candidate in candidate_vote:
            votes = candidate_vote[candidate]
            percentage = votes / num_vote * 100
            print(f"{candidate}: {percentage:.3f}% ({votes})")

    # Determine the winner
    winner = max(candidate_vote, key=candidate_vote.get)
    print("-------------------------")
    print(f'Winner: {winner}')
    print("-------------------------")
