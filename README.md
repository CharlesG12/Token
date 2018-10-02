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
    
    Major Algorithm:
    collection_dict = {}
    for each file under: 
        dict={}
        stream <-- data from the file
        words = stream.split()
        for word in words:
            tokenize(word)    
            stemming(word)
            dict.apped(word)
        collection_dict = merge(dict)
    
    Data Structure for collection dictionary:
        collection_dict = {token, [[docN_1, frequency_1],[docN_2, frequency_2],...]} 
    
    
How to run:
1. Enter into project folder;
    For example: mine is /home/011/c/cx/cxg/IR
2. Run command: pip3 install nltk --user
3. Run command: python3 ./Print_info.py

The result is running on UTDallas Unix machine:

It took 2.246081829071045 seconds for token the collection
The number of tokens in the collection: 195431
The number of distinct tokens in the Cranfield text collection is: 8297
The number of words only appear once in the collection: 3383
The average token per book 139.59
The 30 most frequent words in the collection:
Index  Word      Frequency
0      the       18682
1      of        11312
2      and       5694
3      to        4372
4      in        4245
5      is        4107
6      for       3265
7      are       2425
8      with      2082
9      by        1696
10     at        1591
11     that      1565
12     on        1552
13     flow      1412
14     be        1269
15     an        1258
16     as        1101
17     this      1079
18     from      1067
19     pressure  1021
20     which     968
21     number    905
22     results   873
23     it        851
24     mach      725
25     boundary  722
26     was       698
27     theory    693
28     method    634
29     been      589

After Stemming
The number of tokens in the collection: 195431
The number of distinct stems in the Cranfield text collection is: 5623
The number of stems that occur only once in the Cranfield text collection: 2268
The average token per book 139.59
The 30 most frequent stems in the Cranfield text collection:
Index  Word      Frequency
0      the       18682
1      of        11312
2      and       5694
3      to        4372
4      in        4245
5      is        4107
6      for       3265
7      are       2425
8      with      2082
9      by        1696
10     flow      1598
11     at        1591
12     that      1565
13     on        1552
14     be        1366
15     an        1258
16     number    1236
17     pressur   1180
18     as        1101
19     thi       1079
20     result    1072
21     from      1067
22     it        1029
23     which     968
24     effect    839
25     method    820
26     solut     785
27     theori    780
28     boundari  750
29     equat     732




