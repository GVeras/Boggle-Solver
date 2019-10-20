# Boggle-Solver

A Python program that uses depth-first searching and memorization to solve any user defined Boggle board.

## The Rules
The program follows the traditional Boggle rules and scoring, which is:

**Goal: To make LEGAL english words (using the allEnglishWords.txt file) out of a 3x3,4x4, or 5x5 board of characters.**

Illegal words: 
- Words less than 3 characters.
- No abbrevations allowed. 
- No pronouns. 
- No translated words.
    
The tradional boards are 3x3, 4x4, or 5x5.

**Scoring:**

| Number of Characters in Words | Score per Word Length |
| ------------- | ------------- |
| 3  | 1  |
| 4  | 1  |
| 5  | 2  |
| 6  | 3  |
| 7  | 5  |
| 8+  | 11 |

It's worth noting that Qu replaces Q in this game, and Qu is in one character slot and is worth two characters.

## How to use the program

Python 3.6.5 or higher is required to appropriately use the program.

Under assumption that the user set as an PATH variable and is accessible in any directory, the program can be executed on Windows CMD using:
```
 python solveBoggle.py 3-5 [-n] [-s] [-t] [boardstring]
```
on Linux terminal:
```
 python3 solveBoggle.py 3-5 [-b] [-n] [-s] [-t] [boardstring]
```
Flags (case-sensitive):
 - **3-5:** How many rows and columns the Boggle board will have.
 - **-t:** Show the time it took to execute the input.
 - **-n:** Disable default usage of memorization list. 
 - **-s:** Disable display of score distributions and only show words.
 - **boardstring:** Optionally enter the board in a string with any number of spaces, the order does matter however.
 
 For example the following valid command 
```
python 3 abc def g h q
```
Will be intrepeted as:

| a | b | c |
| - | - | - | 
| d  | e  | f |
| g  | h  | qu |

Without the boardstring option, and solely a number (3-5), the program will ask for each row individually which may be easier to input characters.

**Currently it is recommended to only use 3x3 and 4x4 boards because the program needs to be revised to be more efficient for a 5x5 board due to the high cost of searching for words in a 5x5 board.**

## Current Progress:

- [x] Successfully Search through a 3x3 board.
- [x] Successfully Search through a 4x4 board.
- [ ] Successfully Search through a 5x5 board.

- [x] Score the results accurately.

- [x] Add a Memorization list to lookup past results and record current results.
- [ ] Polish Memorization list.

