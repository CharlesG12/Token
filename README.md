# Token
**Python Implementation of token rule**

`Program performance`
It takes     for program to acquire the text characteristics of cranfield collection.

Program handle scenario
    Upper and lower case word: convert all the words to lower case.
    Words with dashes: remove all the dashes.
    Possessives: remove 's.
    Acronyms: remove .   U.N. becomes UN
    Number: remove all the number
    

Major Algorithms and data structure:
    1. Program load each file from folder, store the document number to an int and article to a string.
        then split string to a list of words by blank. 
    2. Apply TokenRules on each word, and then store in dictionary, word as Key, <docNo, frequency> as value.
    3. Merge all the dictionary based on each doc to a dictionary for the collection.






