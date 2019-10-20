# Boggle-Solver
A Python program that uses depth-first searching and memorization to solve any user defined Boggle board.

## The Rules
The program follows the traditional Boggle rules and scoring, which is:

**Goal: To make LEGAL words out of single CHARACTERS.**

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

Python 3.6+ is required to use the program.

Using the

## Current Progress:

- [x] Successfully Search through a 3x3 board.
- [x] Successfully Search through a 4x4 board.
- [ ] Successfully Search through a 5x5 board.

- [x] Score the results accurately.

- [x] Add a Memorization list to lookup past results and record current results.
- [ ] Polish Memorization list.


