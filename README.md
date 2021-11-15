# Election-Analysis
## Project Overview
A Colorado Board of Elections employee (Seth) has given us the following tasks to complete an audit of the most recent local congressional election.
1. Calculate the total number of votes cast in the election
2. Provide a breakdown of how each county voted in the precinct
3. Provide a breakdown of votes cast for each candidate in the election
4. Determine the winner of the election 
## Resources
* Data Source: election_results.csv
* Software: Python 3.8.8, Spyder 4.2.5
## Election Results 
<img width="280" alt="Election_Results_Terminal" src="https://user-images.githubusercontent.com/93271297/141862175-379c4dce-0f38-4baa-9f6c-573b88341de6.png">

### The analysis of the election shows us that: 
* There were a **total** of **369,711** votes cast in the election
* The number and percentage of votes per county broke down as follows
  * **Jefferson** county cast **10.5%** of the total votes equaling **38,855** votes
  * **Denver** county cast **82.8%** of the total votes equaling **306,05** votes
  * **Arapahoe** county cast **6.7%** of the total votes equaling **24,801** votes
* The number and percentage of votes each candidate received broke down as follows
  * **Charles Casper Stockham** received **23.0%** of the total vote equaling **85,213** votes
  * **Diana DeGette** received **73.8%** of the total vote equaling **272,892** votes
  * **Raymon Anthony** Doane received **3.1%** of the total vote equaling **11,606** votes
* The **WINNER** of the election was:
  * **Diana DeGette**, who received **73.8%** of the vote and **272,892** votes
## Election Audit Summary
  After completing this election analysis we have full confidence in recommeding the utilization of our python scripts for all future election audits. At the core of our script, we were able to use two similarly structured conditional loops to calculate the percentage and total vote count for each candidate in the election as well as for each county in the precint. This allowed us to view valuable data that could determine the outcome of the election. The script's framework could be applied to elections on any scale whether it municipal, state, or federal. Additionally, with minor modifications to the code we can enhance the reach of the analysis to return more data for our users like breaking down the percentage of votes each candidate received within each county.
