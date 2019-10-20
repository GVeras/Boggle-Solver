# Boggle-Solver
A Python program that uses depth-first searching and memorization to solve any user defined Boggle board.

## The Rules
The program follows the traditional Boggle rules and scoring, which is:

###### Goal: To make LEGAL words out of single CHARACTERS. 

Illegal words: 
    1.No abbrevations allowed. 
    2.No pronouns. 
    3.No translated words.
    
The tradional boards are 3x3, 4x4, or 5x5.

###### Scoring:

| Number of Characters in Words | Score per Word Length |
| ------------- | ------------- |
| 3  | 1  |
| 4  | 1  |
| 5  | 2  |
| 6  | 3  |
| 7  | 5  |
| 8+  | 11 |

It's worth noting that Qu replaces Q in this game, and Qu is in one character slot and is worth two characters.
