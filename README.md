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

### Day 6:
a) Just traveling through a maze... i did it just without thinking, straingforward

b) We need to place a something in the way, so that we are endlessly caught in the maze. I did it, but it is a total mess as i use EVERY plot of the maze in my solution. After more thinking, it should be simply enough to use any field which we walked through in solution a. My solution works, but it of course it is very slow and inefficient.

### Day 7:
a) After thinking for a long time (i am getting old) i was able to see, that this is a simple tree-search and therefor a simple recursive solution. After doing the thinking, the implementation is really very easy

b) Ok... just takes 2 more lines - too easy for a part b on day 7 - but ok for an old man ;-)

### Day 8:

a) Not much to say, nothing special, calculating a little bit and checking allready taken positions in the representation of a map

b) Some more calculations, nothing special here either. The only thing which took me some time: to read and understand the exercise ;-)! In contrast to exercise 8a, in 8b the "antennas" needs to be taken into account, but not all of them...  

### Day 9:

a) A bit annoying exercise. I had no good ideas, so i just implemented it straight forward - but it took some time. Playing around with lists... 

b) Same as a... not really difficult, but took me some time because of all the step-by-step looking at what happens. I am getting old ;-)

### Day 10:

a) Ok, nice exercise. It is a kind of breitensuche, recursiv function can solve that. I made the mistake to solve accidently part b), so took some time to read the exercise carefully and solving it afterwards.

b) Ok, after solving part b) accidently, this was done in minutes. But nice.
