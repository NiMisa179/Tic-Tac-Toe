# 1. Description
## Tic-Tac-Toe Game
The classic Tic-Tac-Toe game written in Python by me. The game requires two players, one with 'X' and one with 'O'.
# 2. Features
* The application prints the tic-tac-toe template.
* Using Python lists to store the tic-tac-toe template
* Displays the current state of the table, after each move.
* It throws a message when a player tries to choose an aldready written square.
* It handles tie situation.

# 3. Technologies
* Python3
* Lists
* Loops

# 4. Execute the program
1. Save the script as:
   tic_tac_toe.py
2. Run the program:
   python  tic_tac_toe.py

# 5. Structure
``` text
Tic-Tac-Toe/    

├──  tic_tac_toe.py         # Main program
└── README.md           # Project Documentation
``` 

# 6. Example Output

``` plaintext

Tic Tac Toe!
S T A R T: Y/N?: Y
Player 1: X
Type the number of row you would like to choose: 1
Type the number of column you would like to choose: 1
+---+---+---+
| X |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
Player 2: O
Type the number of row you would like to choose: 1
Type the number of column you would like to choose: 2
+---+---+---+
| X | O |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
Player 1: X
Type the number of row you would like to choose: 2
Type the number of column you would like to choose: 2
+---+---+---+
| X | O |   |
+---+---+---+
|   | X |   |
+---+---+---+
|   |   |   |
+---+---+---+
Player 2: O
Type the number of row you would like to choose: 3
Type the number of column you would like to choose: 1
+---+---+---+
| X | O |   |
+---+---+---+
|   | X |   |
+---+---+---+
| O |   |   |
+---+---+---+
Player 1: X
Type the number of row you would like to choose: 3
Type the number of column you would like to choose: 3
+---+---+---+
| X | O |   |
+---+---+---+
|   | X |   |
+---+---+---+
| O |   | X |
+---+---+---+
Player 1 wins

Process finished with exit code 0

-------------------------------------------------------------
TIE SITUATION:

Tic Tac Toe!
S T A R T: Y/N?: Y
Player 1: X
Type the number of row you would like to choose: 1
Type the number of column you would like to choose: 1
+---+---+---+
| X |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
Player 2: O
Type the number of row you would like to choose: 1
Type the number of column you would like to choose: 2
+---+---+---+
| X | O |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
Player 1: X
Type the number of row you would like to choose: 1
Type the number of column you would like to choose: 3
+---+---+---+
| X | O | X |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
Player 2: O
Type the number of row you would like to choose: 1
Type the number of column you would like to choose: 3
This box has already a value. Please choose another one.
Type the number of row you would like to choose: 2
Type the number of column you would like to choose: 1
+---+---+---+
| X | O | X |
+---+---+---+
| O |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
Player 1: X
Type the number of row you would like to choose: 2
Type the number of column you would like to choose: 3
+---+---+---+
| X | O | X |
+---+---+---+
| O |   | X |
+---+---+---+
|   |   |   |
+---+---+---+
Player 2: O
Type the number of row you would like to choose: 3
Type the number of column you would like to choose: 3
+---+---+---+
| X | O | X |
+---+---+---+
| O |   | X |
+---+---+---+
|   |   | O |
+---+---+---+
Player 1: X
Type the number of row you would like to choose: 2
Type the number of column you would like to choose: 2
+---+---+---+
| X | O | X |
+---+---+---+
| O | X | X |
+---+---+---+
|   |   | O |
+---+---+---+
Player 2: O
Type the number of row you would like to choose: 3
Type the number of column you would like to choose: 1
+---+---+---+
| X | O | X |
+---+---+---+
| O | X | X |
+---+---+---+
| O |   | O |
+---+---+---+
Player 1: X
Type the number of row you would like to choose: 3
Type the number of column you would like to choose: 2
+---+---+---+
| X | O | X |
+---+---+---+
| O | X | X |
+---+---+---+
| O | X | O |
+---+---+---+
It 's a tie!

Process finished with exit code 0


```

# 7. Future Improvements
Some future improvements I keep in mind are:
* to develop GUI
* to develop functions making the code easier to read.
  
# 8. Author
Nikos Misailidis 
Github: https://github.com/nmisailidis
