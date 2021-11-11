#add our dependencies
import csv
import os

# assign a variable for the file to LOAD and the path
file_to_load = 'election_results.csv'

# assign a variable to SAVE the file to a path
file_to_save = os.path.join('Analysis','election_analysis.txt')

#1. Initialize variable for total vote counter 
total_votes = 0   #done before open file so variable resets to 0 each time

#2. initialize variable for list of candidates
candidate_options = []

#3. declare empty dictionary for votes per candidate
candidate_votes = {}

#4. initialize variables for winning candidate, winning count, and winning percentage
winning_candidate = ''
winning_count = 0
winning_percentage = 0


# OPEN the election results and read the file
with open(file_to_load) as election_data: 
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    # Set headers variable and then read headers
    headers = next(file_reader)

    # print each row in the CSV file
    for row in file_reader:
        #add to the total vote count
        total_votes += 1
        
        #print the candidate name from each row using indexing
        candidate_name = row[2]
        
        # if the candidate does not match any existing candidates
        if candidate_name not in candidate_options:
            #add candidate name to listo of candidate options
            candidate_options.append(candidate_name)
            
            #create each candidate as a key and set to 0 to begin vote count
            candidate_votes[candidate_name]=0
            
        #add to candidate's vote count, align with if-statement but inside for-loop
        candidate_votes[candidate_name] += 1
    
# save the results to our text file
with open(file_to_save, 'w') as txt_file:
    #print the final vote count to the terminal
    election_results = (
           f'\nElection Results\n'
           f'------------------------\n'
           f'Total Votes: {total_votes:,}\n'
           f'------------------------\n')
    print(election_results, end='')
    #Save the final vote count to the text file
    txt_file.write(election_results)
     
    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. set variable for results and Print the candidate name and percentage of votes.
        candidate_results = f"{candidate_name}: received {vote_percentage:.1f}% ({votes:,})\n"
        print(candidate_results)
        # Save the candidate results to txt file
        txt_file.write(candidate_results)

        # Determine winning vote count, percentage, and candidate
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
    #Print winning candidates results       
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)
    
    #save the winning candidate's results to txt file
    txt_file.write(winning_candidate_summary)



        
    
        