# Modules
import os
import csv


# Set path for file
csvpath = os.path.join( "Resources", "election_data.csv")

#Initiate Variables
vote_count = 0
candidate_list = []
votes_list = []



# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for row in csvreader:
      vote_count += 1

      #Make the List of Candidates
      if row[2] not in candidate_list:
         candidate_list.append(row[2])
         votes_list.append(0)

      
      index_candiadte = list.index(candidate_list,row[2])
 
       #Count the Vote for each candidate
      votes_list[index_candiadte] += 1


#Who is the Winner
winner = votes_list[0]
for candidate in votes_list:
   if candidate >= winner:
      winner = candidate
print(winner)

index_winner = votes_list.index(winner)



# Numbers of lines for the print
num_lines = 40
line_form = "-"
percentage_vote = []
print("Election Results")


print(line_form*num_lines)
print("Total Votes: " + str(vote_count))
print(line_form*num_lines)
#Calculate the Percentages of votes


for percentage in votes_list:
   percentage_vote.append(percentage/vote_count)
i = 0
for candidate in candidate_list:
   print(str(candidate) + ": " +"{:.2%}".format(percentage_vote[i]) + "    " + "(" + str(votes_list[i])+")" )
   i += 1

print(line_form*num_lines)

#Who is the Winner
print("Winner: " + str(candidate_list[index_winner]))

print(line_form*num_lines)




# Specify the file to write to
output_path = os.path.join("Analysis", "Results.csv")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:
      #  # Initialize csv.writer
   csvwriter = csv.writer(csvfile, delimiter=' ')
   csvwriter.writerow(['Election Results'])
   csvwriter.writerow([line_form*num_lines])

   i = 0
   for row in candidate_list:
      csvwriter.writerow([row,":" ,"{:.2%}".format(percentage_vote[i]), votes_list[i]])
      i += 1

   csvwriter.writerow([line_form*num_lines])

   csvwriter.writerow(["Winner: ",candidate_list[index_winner]])
   csvwriter.writerow([line_form*num_lines])

