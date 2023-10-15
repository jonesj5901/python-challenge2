import os
import csv

electionCsv = os.path.join("PyPoll", "Resources", "election_data.csv")

with open(electionCsv) as csvFile:
    # get the wrapper and store it as a reader using the .reader() function
    csvReader = csv.reader(csvFile, delimiter=",")

    csvHeader = next(csvReader)

    ballotID = []
    candidates = []
    num = []
    votes = []
    percent = []

    for row in csvReader:
        ID = row[0]
        county = row[1]
        candidate = row[2]
        ballotID.append(ID)
        totalVotes = len(ballotID)
        num.append(candidate)
        if candidate not in candidates:
            candidates.append(candidate)
    numCan = len(candidates)    

    for row2 in range (0, numCan):
        name = candidates[row2]
        votes.append(num.count(name))
        percentVote = votes[row2]/totalVotes
        percent.append(percentVote) 

    winner = votes.index(max(votes))  


with open("PyPoll.txt", "wt") as f:
    print(f"Election Results", file = f)
    print("-------------------------", file = f)
    print(f"Total Votes: ${totalVotes}", file = f)
    print(f"-------------------------", file = f)
    for row3 in range (0, numCan): 
        print(f"{candidates[row3]}: {percent[row3]:.3%} ({votes[row3]:,})", file = f)
    print(f"-------------------------", file = f)
    print(f"Winner: {candidates[winner]}", file = f)
    print(f"-------------------------", file = f)