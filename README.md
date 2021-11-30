# Election_Analysis

##Project_Overview

Colorado Board of Elections gives us a set of tasks to complete an election audit of a recent local election

Steps to follow:
1. Calculate total votes cast
2. Get a complete list of candidates
3. Calculate total votes each candidate received
4. Calculate percentage of votes for each candidate
5. Determine the winner based on popular vote

## Resources
- Provided documents such as election_results.csv

# Summary
Through analysis we were able to determine and filter out the name of candidates and how many votes they received
Candidates were as follows:
1. Charles Casper Stockham 
2. Diana DeGette (Winner)
3. Raymon Anthony Doane

- Candidate Results:
- CCS Received 23% of vote with 85,213 votes
- DDG Received 73.8% of vote with 272,892 votes 
- RAD received 3.1% of vote with 11,606 votes


### Overview of Election Audit
 Purpose of this audit was to be able to use automated methods to filter through data and determine the winner of an election while calculating voter turnouts and percentages.
 
 # Amount of votes cast in this election: 369,711
 
 # Provide breakdown on number of votes and percentage of total votes for each county
 -    Arapahoe:  6.7%  (24,801 votes)
 -    Denver:    82.8% (306,055 votes)
 -    Jefferson: 10.5% (38,855 votes)
 
 # Which county had largest number of votes? : Denver
 
 # Provide a breakdown of number of votes and pct each candidate received:
 -  Charles Casper Stockham: 23.0% (85,213)
 -  Diana DeGette: 73.8% (272,892)
 -  Raymon Anthony Doane: 3.1% (11,606)

# Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
-   Diana DeGette: 73.8% (272,892)

## Election Audit Summary
Through easy and simple modifications of this script, it can be manipulated to calculate voting percentages and candidate winners for any election. 
By changing the path locations and name of the files that are being fetched one can filter through similarly formatted csv files and save them to an easy to read text file.

### Challenges faced
My biggest challenge overall was not being able to change the output of the Arapahoe being placed over every county name. The votes and percentages were correct but it did not distinguish between counties. I thought this could be due to the for loop not appending county names to the list correctly but it looked fine to me and using a print command I was able to see that the code did print out the correct counties the correct am't of times when iterating through the loop. 

I also faced a challenge of creating hard to memorize variable names which confused me to an extent. Through simplification of variable names I was able to then distinguish between values and variables a lot easier.
