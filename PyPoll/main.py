import os 
import csv

csvpath = os.path.join("/Users/aosmacbookpro/Desktop/gitlab-data-analytics/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv")


tot_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0


with open(csvpath,newline="", encoding="utf-8") as votes:

    csvreader = csv.reader(votes,delimiter=",") 

    
    header = next(csvreader)     

    
    for row in csvreader: 

        tot_votes +=1

        if row[2] == "Khan": 
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes,li_votes,otooley_votes]

cand_and_votes = dict(zip(candidates,votes))
key = max(cand_and_votes, key=cand_and_votes.get)


khan_percent = (khan_votes/tot_votes) *100
correy_percent = (correy_votes/tot_votes) * 100
li_percent = (li_votes/tot_votes)* 100
otooley_percent = (otooley_votes/tot_votes) * 100

# Print the summary table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {tot_votes}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

# Output files
# Assign output file location and with the pathlib library
output_file = os.path.join("Final Summary.txt")

with open(output_file,"w") as file:

# Write methods to print to Elections_Results_Summary 
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {tot_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Khan: {khan_percent:.3f}% ({khan_votes})")
    file.write("\n")
    file.write(f"Correy: {correy_percent:.3f}% ({correy_votes})")
    file.write("\n")
    file.write(f"Li: {li_percent:.3f}% ({li_votes})")
    file.write("\n")
    file.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")



