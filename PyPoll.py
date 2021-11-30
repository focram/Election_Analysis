import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("election_results.csv")

#create a filename variable to a direct or indirect path to the file.

file_to_save = os.path.join("analysis", "election_analysis.txt")



#Initialize a vote counter
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     file_reader = csv.reader(election_data)

     #Read and print the header row
     headers = next(file_reader)
     
     for row in file_reader:
         #add to the total vote count
        total_votes +=1
        
        #print the candidate name from each row
        candidate_name = row[2]

        #Add the candidate name to the candidate options list.
        if candidate_name not in candidate_options:  #checks if name is already in the list
            #if candidate name already in list it will not print again to avoid overprinting
            candidate_options.append(candidate_name)
            
            #Begins tracking the candidates vote count and sets them all to 0
            candidate_votes[candidate_name] = 0
            
        #Add a vote to the candidate count
        candidate_votes[candidate_name] += 1

        #Save results to our text file
with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    #save the final vote count to the text file.
    txt_file.write(election_results)
    


    #iterate through the candidate list
    for candidate_name in candidate_votes:

            #Retrieve the vote count of candidate.
        votes = candidate_votes[candidate_name]

            #Calculate the percentage of votes, use float bc percentage will be decimal
        vote_percentage = float(votes)/float(total_votes) *100
        rounded_vote = round(vote_percentage, 1)
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

            #To do: print out each candidates name, vote count and pct of votes to terminal
            ##print(f"{candidate_name}: {rounded_vote}%: ({votes:,})\n ")
            #determine winning vote and candidate
            #Determine if the votes is greater than the winning count.
        if(votes > winning_count) and (vote_percentage > winning_percentage):
                #1. If true then set winning_count = votes and winning_percent
                winning_count = votes

                # 2. vote_percentage.
                winning_percentage = vote_percentage

                #3. Set thhe winning_candidate equal to the candidates name.
                winning_candidate = candidate_name

    winning_candidate_summary = (
                f"-------------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"-------------------------\n")
    print(winning_candidate_summary)

                        
    txt_file.write(winning_candidate_summary)         
           

            #Using the open() function with the "w" mode we will write data to the file

            #open(file_to_save, "w")

            #Use the open statement to open the file as a text file
            #outfile = open(file_to_save, "w")
        