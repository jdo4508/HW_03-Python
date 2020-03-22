# You will be give a set of poll data called election_data.csv.
# The dataset is composed of three columns: Voter ID, County, and Candidate. 
# Your task is to create a Python script that analyzes the votes and 
# calculates each of the following:
#     The total number of votes cast
#     A complete list of candidates who received votes
#     The percentage of votes each candidate won
#     The total number of votes each candidate won
#     The winner of the election based on popular vote.

# Import OS & CSV
import os
import csv
import sys

#Create list for each column
votes = []
candidate_name = []
Khan = []
Correy = []
Li = []
Otooley = []

# Create path from resources folder
filepath = os.path.join ('..', 'Resources', 'election_data.csv')

# Read in CSV file
with open (filepath, 'r') as csvfile:
    csvreader = csv.reader (csvfile, delimiter = ',')
    #print(csvreader)

# Define first row as header
    csv_header = next(csvreader)
    #print(f"Header: {csv_header}")

# Append values to lists
    for row in csvreader:
        votes.append(int(row[0]))
        candidate_name.append(row[2])

# Calculate total number of votes
    total_votes = (len(votes))
    # print(total_votes)

# Tally number of votes for each candidate name
###I feel like i cheated here by knowing the candidate names...if there was another name buried in the data I would miss it!
    for name in candidate_name:
        if name == "Khan":
            Khan.append(candidate_name)
            Khan_votes = len(Khan)
         
        elif name =="Correy":
            Correy.append(candidate_name)
            Correy_votes = len(Correy)
 
        elif name =="Li":
            Li.append(candidate_name)
            Li_votes = len(Li)

        else:
            Otooley.append(candidate_name)
            Otooley_votes = len(Otooley)
           
    # print("Khan Votes:" + str(Khan_votes))
    # print("Correy Votes:" + str(Correy_votes))
    # print("Li Votes:" + str(Li_votes))
    # print("Otooley Votes:" + str(Otooley_votes))

# Determine percent of total vote by candidate 
percent_Khan = ((Khan_votes / total_votes) * 100)
# print("Khan Percent:" + str(percent_Khan) + "%")
percent_Correy = ((Correy_votes / total_votes) * 100)
# print("Correy Percent:" + str(percent_Correy) + "%")
percent_Li = ((Li_votes / total_votes) * 100)
# print("Li Percent:" + str(percent_Li) + "%")
percent_Otooley = ((Otooley_votes / total_votes) * 100)
# print("Otooley Percent:" + str(percent_Otooley) + "%")

# Determine popular vote winner
if Khan_votes > max(Correy_votes, Li_votes, Otooley_votes):
    winner = "Khan"
    # print("Khan Wins")
elif Correy_votes > max(Khan_votes, Li_votes, Otooley_votes):
    winner = "Correy" 
    # print("Correy Wins") 
elif Li_votes > max(Correy_votes, Khan_votes, Otooley_votes):
    winner = "Li"
    # print("Li Wins")
else:
    winner = "O'Tooley"
    # print("O'Tooley Wins")   

# Print final parameters
## Decimal formatting will def be the death of me...tried round but kept getting error!

print("Election Results")
print(f"Total Votes: {total_votes}")
print(f"Khan: {percent_Khan}% ({Khan_votes})")
print(f"Correy: {percent_Correy}% ({Correy_votes})")
print(f"Li: {percent_Li}% ({Li_votes})")
print(f"O'Tooley: {percent_Otooley}% ({Otooley_votes})")
print(f"Winner: {winner}")

#Create output .txt file
##blarrgggghhhhh i looked this up and it works but not how we did it in class!
sys.stdout = open("election_results.txt", "w")
print("Election Results")
print(f"Total Votes: {total_votes}")
print(f"Khan: {percent_Khan}% ({Khan_votes})")
print(f"Correy: {percent_Correy}% ({Correy_votes})")
print(f"Li: {percent_Li}% ({Li_votes})")
print(f"O'Tooley: {percent_Otooley}% ({Otooley_votes})")
print(f"Winner: {winner}")
sys.stdout.close()