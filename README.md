# Boggle-Solver

A Python program that uses depth-first searching and memorization to solve any user defined Boggle board.

## The Rules
The program follows the traditional Boggle rules and scoring, which is:

**Goal: To make LEGAL english words (using the allEnglishWords.txt file) out of a 3x3, 4x4, or 5x5 board of characters.**

Words are made by starting at any letter on the board, and "connecting" other letters to make a word, letters can only be connected if they are adjacent. This **includes** letters that are diagonal of each other.

Illegal words: 
- Words less than 3 characters.
- No abbrevations allowed. 
- No pronouns. 
- No translated words.
    
The tradional boards are 3x3, and 4x4.

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

Download **all** the files in the repo, do not edit any of the .txt files.

Python 3.6.5 or higher is required to appropriately use the program.

Under assumption that the user set as an PATH variable and is accessible in any directory, the program can be executed on Windows CMD using:
```
 python solveBoggle.py 3-4 [boardstring] [-n] [-s] [-t]
```
on Linux terminal:
```
 python3 solveBoggle.py 3-4 [boardstring] [-n] [-s] [-t] 
```
Flags (case-sensitive, and any order/combination works.):
 - **3-4:** How many rows and columns the Boggle board will have.
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


