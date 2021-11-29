import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)


#create a filename variable to a direct or indirect path to the file.

file_to_save = os.path.join("analysis", "election_analysis.txt")

#Using the open() function with the "w" mode we will write data to the file

open(file_to_save, "w")