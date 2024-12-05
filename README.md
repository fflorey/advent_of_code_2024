# advent_of_code_2024
final fun in 24

Project is created before 1st of December, i am raedy to support the elves!

### Day 1: 

a) Sort and add differences and result of some multiplications

b) Simply count some numbers, nothing to say here

### Day 2: 
a) Analyze sequences of integer values - stetigkeit and smooth in- or decrease. Lots of comparisons and handling if indices
b) My solution is a little bit brute force - just create all possible lines by deleting one character at a time
### Day 3: 
a) Just find all "mul(X,Y)" and execute these multiplications - can be done easily by using regular expressions

b) Interpretation of do() and don't() - i just deleted the text sequences with my text editor (vi) - and used the 3a-solution afterwards. So, no 3b here

### Day 4:
a) Finding: "XMAS"-Strings forward, backward, up, down, diagonal in a 2-dimensional character-array. I used just from left to right and one diagonal sequence, then turning the matrix by 90 degrees (three times).

b) Same with 4b: Just find "MAS" from top left to bottom right and bottom left to top right - then turn the matrix by 90 degrees times (three times).

### Day 5:
a) Many rules ("page ordering rules") between integers can be interpreted as a directed graph. If you do so and create such graph (easy with Python and nx-library), you can simply check the validity of a sequence of numbers by checking if the necessary edges exists

b) The incorrect sequences must be corrected: start from beginning of the sequence and if there is no edge between to nodes, just exchange the nodes and try again for the sequence. This solution is possible, because we know that **every** sequence can be corrected. 


