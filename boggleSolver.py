###
#  Made by: Gabriel Veras
#  A Boggleboard solver, see the all the details in the README.md on GitHub at: https://github.com/GVeras/Boggle-Solver
###

import sys
import time

# A DFS of this scale (millions of possible strings), requires a high recursion limit for Python. This limit sets the default (1000) to 100,000 instead. 
# Most modern computers will be able to handle this recusion limit.

sys.setrecursionlimit(10**5) 


### Functions

# A helper function to the mergeSort function to combine and sort two arrays simultaneously.
def combine(array1,array2):
	index2=index1=0
	rtnArray=[]
	while index1!= len(array1) and index2!=len(array2):
		if array1[index1]>array2[index2]:
			rtnArray.append(array2[index2])
			index2+=1
		else:
			rtnArray.append(array1[index1])
			index1+=1
	rtnArray.extend(array1[index1:])
	rtnArray.extend(array2[index2:])
	return rtnArray

# A basic sorting function to sort the searched words.
def mergeSort(array):
	middle=len(array)//2
	left=array[:middle]
	right=array[middle:]
	if len(left)!=1:
		left=mergeSort(left)
	if len(right)!=1:
		right=mergeSort(right)
	return combine(left,right)

# A function to convert the 2D array into a single string.
def boardToString(board):
    rtnString=""
    for row in board:
        for item in row:
            rtnString+=item
    return rtnString

### Parsing Arguments

# Intial arguments to decide how the output is displayed with the given arguments.
boardRowSize = 0
timer=False
scoreDist=True
memorize=True
sOrB='b'
inputString=""

for argument in sys.argv:
    if argument=="python" or argument=="boggleSolver.py" or argument=="python3": 
        continue
    elif argument.isnumeric() and boardRowSize==0:
        argument=int(argument)
        if argument>2 and argument<6:
            boardRowSize=argument
    elif argument.startswith('-'):
        if argument=="-n":
            memorize=False
        elif argument=="-s": 
            scoreDist=False
        elif argument=="-t": 
            timer=True
    elif argument.isalpha:
        sOrB='s'
        inputString+=argument


### Error handling.

if boardRowSize==0:
    sys.exit("\nNo board size detected.")
if boardRowSize==5:
    sys.exit("\nA 5x5 board is not supported at this time.")

### Searching the English dictionary
inputFile=open('allEnglishWords.txt','r')

engWords=set()
for line in inputFile:
    line=line.strip("\n")
    line=line.lower()
    engWords.add(line)
inputFile.close()


### Interpret input and initialize board.
sOrB=sOrB.lower()
boggleboard=[]

# Parsing multiple rows of strings as input
if sOrB=='b':
 for x in range(boardRowSize):
    singleLine=input("Enter a row of "+str(boardRowSize)+" characters here (spacing doesnt matter): ")
    multipleChars=[] 
    count=0
    for char in singleLine:
        if count==boardRowSize:
            break
        elif char.isalpha():
            if char.lower()=='q':
                multipleChars.append('qu')
            else:
                multipleChars.append(char.lower())
            count+=1
    boggleboard.append(multipleChars)

# Parsing a single string as input
elif sOrB=='s':
    count=0
    if len(inputString)!=boardRowSize**2:
        sys.exit("\nIncorrect number of chracters. There is supposed to be: "+str(boardRowSize**2)+", yet there is: "+str(len(inputString)))
    while (count!=boardRowSize**2):
        currentRow=[]
        while (len(currentRow)!=boardRowSize):
            if inputString[count].lower()=="q":
                currentRow.append("qu")
            else:
                currentRow.append(inputString[count].lower())
            count+=1
        boggleboard.append(currentRow)
            
else:
    sys.exit("Error reading input...")

### Print the entire board
print("\nThe board:")
for row in boggleboard:
    print("\t",row)

start_time = time.time()

### Key information before starting the Depth First Search
boardRows=len(boggleboard)
boardColumns=len(boggleboard[0])
position=[0,0]

### The directions for searching the board, the arrows are just for visualization
directions=[
    [0,-1,"←"],
    [-1,-1,"↖"],
    [-1,0,"↑"],
    [-1,1,"↗"],
    [0,1,"→"],
    [1,1,"↘"],
    [1,0,"↓"],
    [1,-1,"↙"],
]


def boardToString(board):
    rtnString=""
    for row in board:
        for item in row:
            rtnString+=item
    return rtnString


### Depth-first search function that appends all the words to one big array.
def possibleWords(boggleboard,boardRows,boardColumns,position,visited,string,depth):
    # Bare in mind that the (x,y) coordinates are a bit odd for this, they can be described as on a (y,x) plane rather than a traditional (x,y) plane due to the way indices work.
    
    allWords=[string] # This is a string that first contains the character provided, then it will cumulatively add more letters the deeper it gets in the search. 
    
    adjCoordinates=[] # Empty 2D array to hold valid indices (as in not out of bounds indices).

    for dir in directions:     #Check all 8 directions.
          ySum=dir[0]+position[0] #Add each direction to the current position to a sum that is where an alleged adjacent character could be.
          xSum=dir[1]+position[1] 

          #Check for valid indices amount the X,Y pairs given are a valid index then append the index to the adjacent characters list.
          if not ( (ySum<0 or xSum<0) or (ySum>=boardRows) or (xSum>=boardColumns) ) and [ySum,xSum] not in visited:
              adjCoordinates.append([ySum,xSum])
    
    # Visited starts empty and cumulatively adds more visited indexes the deeper it gets. 
    visited.append(position) 

    # Search valid adjacent coordinate.
    for coor in adjCoordinates: 

        # Recursively search the adjacent characters, creating new instances of strings and returning all the strings into an array.
        allWords+=possibleWords(boggleboard,boardRows,boardColumns,coor,visited,string+boggleboard[coor[0]][coor[1]],depth+1)

        # Once the search goes as deep as it can, delete the previous "batch" of visited indices, as to allow new search instances to be created.
        del visited[depth+1:]

    return allWords

### Search the memorization list to see if the board was already solved in the past
mem=open("pastBoards.txt",'r')
pastBoards={}
pastLine=""
isKey=True
for line in mem:
    line=line.strip("\n").lower()
    if isKey:
        pastLine=line
        isKey=False
    else:
        if len(line)>1:
            pastBoards[pastLine]=line.split()
        else:
            pastBoards[pastLine]=""
        isKey=True
mem.close()

if memorize==False:
    pastBoards={}

if not (boardToString(boggleboard) in pastBoards):
# Run if it was not found in the memorized list
 totalWords=[]
 # Each character in the 2D array is the starting point for the search in the for-loop below. The position is dynamically changed to get all the characters in the board.
 for row in boggleboard:
     for char in row:
        # The DFS is executed here.
        # For reference: possibleWords(boggleboard,boardRows,boardColumns,position,visited,string,depth):
        totalWords.append(possibleWords(boggleboard,boardRows,boardColumns,position,[],char,0))
        position[1]+=1
     position[1]-=boardColumns
     position[0]+=1
 madeWords=[]
 totalCount=0

# Once the DFS is done, the for-loop below will check the english words set to see if there is any matches.
 for wordRow in totalWords:
    for word in wordRow:
        totalCount+=1
        if len(word)<=2: # As per the rules, the words have to have a length of 3 at least to be considered full english words
            continue
        if word in engWords: 
            madeWords.append(word)
 if len(madeWords)!=0:
  madeWords=mergeSort(list(set(madeWords)))
 memW=open("pastBoards.txt",'a')
 memW.write(boardToString(boggleboard)+"\n")

 if len(madeWords)!=0:
     memW.write(' '.join(madeWords)+"\n")
 else:
     memW.write("\n") 
 memW.close()
else:
    print("\nAlready answered before!")
    madeWords=pastBoards[boardToString(boggleboard)]

### Score Distributions - scoring info is available on the README.md as mentioned at the top of this file.

if len(madeWords)!=0:
    print("\n"+str(len(madeWords))+" english words: ",madeWords,"\n")
    
    score=0
    for word in madeWords:
        currScore=0
        if len(word)==3 or len(word)==4:
            currScore=1
        elif len(word)==5:
            currScore=2
        elif len(word)==6:
            currScore=3
        elif len(word)==7:
            currScore=5
        elif len(word)>7:
            currScore=11

        score+=currScore
        if scoreDist:
            print(word,"=",str(currScore)+"pts",end=" || ")

    print("\n\nTotal Possible Score: %i" % score)
else:
    print("\nNo english words were made from the given board.")

if timer:
    print("\n\n%s seconds for this board to be completely solved." % (time.time() - start_time))
