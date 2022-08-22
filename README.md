# Application-that-will-calculate-the-ranking-table-for-a-league.

So the job of the script is to open the file which contains matches results.
First of all , it will extract all the team names and create a dictionary with the teams name and giving all of them 0 points at the start.
And then , it will read the file given line by line , splits the teams names and scores , and does a comparison , if its a tie then 1 point for each team , if it's not then 3 points to the winners and 0 to the loser .
Finally , the script will search for duplicates , if found , it will delete them from the dict , rearrange then re-insert it back to a new dict with everything .
Then a for loop to show the output in a proper form .
