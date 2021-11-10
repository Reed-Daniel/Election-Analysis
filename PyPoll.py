#add our dependencies
import csv
import os

# assign a variable for the file to LOAD and the path
file_to_load = 'election_results.csv'

# assign a variable to SAVE the file to a path
file_to_save = os.path.join('Analysis','election_analysis.txt')

# OPEN the election results and read the file
with open(file_to_load) as election_data: 
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    # Set headers variable and then print headers
    headers = next(file_reader)
    print(headers)

        
    
        