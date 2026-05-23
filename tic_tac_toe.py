print("Tic Tac Toe!")
ans = input("S T A R T: Y/N?: ")

# creates a 2-dimension list full of empty spaces. 3x3, like the tic-tac-toe board
tic = [[" " for i in range(3)],
       [" " for i in range(3)],
       [" " for i in range(3)]
       ]

# Future Improvement: The game will ask the players if they will continue after the first round
cont = True

win1 = win2 = False

while cont:

    print("Player 1: X")
    row1 = int(input("Type the number of row you would like to choose: "))
    while row1 < 1 or row1 > 3:                                           # checks if the selected row is in the board range
        row1 = int(input("The number of row must be between 1 and 3: "))

    col1 = int(input("Type the number of column you would like to choose: "))
    while col1 < 1 or col1 > 3:                                           # checks if the selected column is in the board range
        col1 = int(input("The number of col must be between 1 and 3: "))

    # checks if the selected cell is empty. If so, write the character (line 30), if not choose another one
    while tic[row1 - 1][col1 - 1] != " ":
        print("This box has already a value. Please choose another one.")
        row1 = int(input("Type the number of row you would like to choose: "))
        col1 = int(input("Type the number of column you would like to choose: "))

    tic[row1 - 1][col1 - 1] = "x"

    # prints the board at its current state
    print("+---+---+---+")
    for i in range(3):
        for j in range(3):
            print("| " + tic[i][j].upper(), end=" ")
        print("|")
        print("+---+---+---+")

    # checks every winning situation for player 1
    if (tic[0][col1 - 1] == tic[1][col1 - 1] == tic[2][col1 - 1] == "x") or (
            tic[row1 - 1][0] == tic[row1 - 1][1] == tic[row1 - 1][2] == "x") or (
            tic[0][0] == tic[1][1] == tic[2][2] == "x") or (tic[0][2] == tic[1][1] == tic[2][0] == "x"):
        win1 = True

    # if the player 1 wins, the game is stopped
    if win1:
        print("Player 1 wins")
        cont = False
        break

    # if an empty cell is spotted, it allows the program to continue.
    # Else, it means that the board is full, and it 's a tie between players.
    cont = False
    for i in range(3):
        for j in range(3):
            if tic[i][j] == " ":
                cont = True
    if not cont:
        print("It 's a tie!")
        break

    print("Player 2: O")
    row2 = int(input("Type the number of row you would like to choose: "))
    while row2 < 1 or row2 > 3:                                             # checks if the selected row is in the board range
        row2 = int(input("The number of row must be between 1 and 3: "))

    col2 = int(input("Type the number of column you would like to choose: "))
    while col2 < 1 or col2 > 3:                                             # checks if the selected column is in the board range
        col2 = int(input("The number of col must be between 1 and 3: "))

    # checks if the selected cell is empty. If so, write the character (line 68), if not choose another one
    while tic[row2 - 1][col2 - 1] != " ":
        print("This box has already a value. Please choose another one.")
        row2 = int(input("Type the number of row you would like to choose: "))
        col2 = int(input("Type the number of column you would like to choose: "))

    tic[row2 - 1][col2 - 1] = "o"

    # prints the board at its current state
    print("+---+---+---+")
    for i in range(3):
        for j in range(3):
            print("| " + tic[i][j].upper(), end=" ")
        print("|")
        print("+---+---+---+")

    if (tic[0][col2 - 1] == tic[1][col2 - 1] == tic[2][col2 - 1] == "o") or (
        tic[row2 - 1][0] == tic[row2 - 1][1] == tic[row2 - 1][2] == "o") or (
        tic[0][0] == tic[1][1] == tic[2][2] == "o") or (tic[0][2] == tic[1][1] == tic[2][0] == "o"):
        win2 = True

    # if the player 2 wins, the game is stopped
    if win2:
        print("Player 2 wins")
        cont = False
        break

    cont = False
    for i in range(3):
        for j in range(3):
            if tic[i][j] == " ":
                cont = True
    if not cont:
        print("It 's a tie!")
        break







