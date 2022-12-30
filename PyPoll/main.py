# read csv file
import os
import csv

pollData = os.path.join("Resources", "election_data.csv")

with open(pollData) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader, None)
    
    # crete list of votes comprised of candidate names
    votes = [str(row[2]) for row in csvreader]

# count the number of unique candidates
candidates = []

for i in votes:
    if i not in candidates:
        candidates.append(i)


# calculate number of votes for each candidate
votetally = []

for i in range(0,len(candidates)):
    votetally.append(0)
    for j in votes:
        if candidates[i] == j:
            votetally[i] += 1


# print all results to terminal
print(f"Total Votes: {len(votes)}")

for i in range(0,len(candidates)):
    print(f"{candidates[i]}: {str(round((votetally[i]/len(votes))*100,2))}% {str(votetally[i])}")

print(f"Winner: {candidates[votetally.index(max(votetally))]}")


# print results to a text file
with open('analysis/pollresults.txt', 'w') as f:
    l1 = f"Total Votes: {len(votes)} \n"
    l2 = []
    for i in range(0,len(candidates)):
        l2.append(f"{candidates[i]}: {str(round((votetally[i]/len(votes))*100,2))}% {str(votetally[i])} \n")
    l3 = f"Winner: {candidates[votetally.index(max(votetally))]}"
    f.writelines([l1, l2[0], l2[1], l2[2], l3])