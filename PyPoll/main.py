#Module 3 Challenge
#Analyze election_data.csv. Dataset contains three columns: ballot ID, County and candidate
#values are separated by ','
#FIND:
#The total number of votes cast 
#A complete list of candidates who received votes 
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote

#import modules
import os
import csv

#set incoming file path
election_data_csv = os.path.join(".", 'Resources', "election_data.csv")

#set outgoing file path
election_output = os.path.join("." "election_results.txt")

#setup variables
total_votes = 0

#define a dictionary to hold [Candidate: votes]
candidate_list = {}

#open and read the csv file
with open(election_data_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    #skip the header
    csv_header = next(csv_reader)

    #loop through the rows to...
    for row in csv_reader:
        
        #find total votes
        total_votes = total_votes + 1
        
        #find location of candidates
        candidate_name = row[2]
        
        #counts votes if candidate is on the list
        if candidate_name in candidate_list:
            candidate_list[candidate_name] += 1
        #adds candidate if not on list, then counts votes
        else:
            candidate_list[candidate_name] = 1

#assign variables to each key:value set
for candidate_name in candidate_list:
    if candidate_name == "Charles Casper Stockham":
        charles_votes = candidate_list[candidate_name]
    elif candidate_name == "Diana DeGette":
        diana_votes = candidate_list[candidate_name]
    elif candidate_name == "Raymon Anthony Doane":
        raymon_votes = candidate_list[candidate_name]

#formula for percent
charles_percent = round((charles_votes / total_votes) * 100, 3)
diana_percent = round((diana_votes / total_votes) * 100, 3)
raymon_percent = round((raymon_votes / total_votes) * 100, 3)

#find the winner
election_winner = max(candidate_list, key=candidate_list.get)

#print to Terminal, use a var to call easier for text output
output = (
    f"\nElection Results\n"
    f"-------------------------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------------------------\n"
    f"Charles Casper Stockham: {charles_percent}% ({charles_votes})\n"
    f"Diana DeGette: {diana_percent}% ({diana_votes})\n"
    f"Raymon Anthony Doane: {raymon_percent}% ({raymon_votes})\n"
    f"-------------------------------------------\n"   
    f"Winner: {election_winner}\n"
    f"-------------------------------------------\n"   
        )

#print output to terminal
print(output)

#export and print to text file
with open(election_output, "w") as txt_file:
    txt_file.write(output)