import csv

with open("/Users/nguyengiang/Downloads/Starter_Code-4/PyPoll/Resources/election_data.csv","r") as csv_file:

    election_csv = csv.DictReader(csv_file)

    num_vote = 0
    candidate_list = []
    candidate_vote = {}

    for row in election_csv:
        num_vote += 1
        candidate = row['Candidate']
        if candidate not in candidate_list:
            candidate_list.append(candidate)
        if candidate not in candidate_vote:
            candidate_vote[candidate] = 1
        else:
            candidate_vote[candidate] +=1

    print(f'Election Results')
    print("-------------------------")
    print(f'Total Vote: ' + str(num_vote))
    print("-------------------------")

    for candidate in candidate_vote:
            votes = candidate_vote[candidate]
            percentage = votes / num_vote * 100
            print(f"{candidate}: {percentage:.3f}% ({votes})")

    winner = max(candidate_vote, key=candidate_vote.get)
    print("-------------------------")
    print(f'Winner: {winner}')
    print("-------------------------")
