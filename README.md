# Assignment 3

## Working with NLP Data

For this project we did the following:

1. The webscraper program from Assignment 2 was run and the resulting data files were posted on the discussion board.

2. Downloaded all 3 text files from the discussion board to the Data/ directory.

3. Created a function that loads the data in the file provided the file path as input parameter.

4. Wrote a script to:

    +   call the file load function for each file (file paths hard coded in this case), 
    
    +   combine them into a single dataframe, 
    
    +   sort them to get the 10 "best" and 10 "worst" companies based on sentiment analysis of their company purpose, 
    
    +   and print the results.

5. The script can be run from the command line using the following command:

         $python main.py

_Notes:_

_One file could not be processed as it did not clearly differentiate between the Company Name and Purpose and was mixed in with other attributes like CEO, Advisor, etc that made it difficult to parse the information needed._


