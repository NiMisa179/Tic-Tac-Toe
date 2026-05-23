print("Tic Tac Toe!")
ans = input("S T A R T: Y/N?: ")
tic = [[" " for i in range(3)],
       [" " for i in range(3)],
       [" " for i in range(3)]
       ]
cont = True
while ans.upper() == "Y":

    while cont:

        print("Player 1: X")
        row1 = int(input("Type the number of row you would like to choose: "))
        while row1 < 1 or row1 > 3:
            row1 = int(input("The number of row must be between 1 and 3: "))

        col1 = int(input("Type the number of column you would like to choose: "))
        while col1 < 1 or col1 > 3:
            col1 = int(input("The number of col must be between 1 and 3: "))

        while tic[row1 - 1][col1 - 1] != " ":
            print("This box has already a value. Please choose another one.")
            row1 = int(input("Type the number of row you would like to choose: "))
            col1 = int(input("Type the number of column you would like to choose: "))

        tic[row1 - 1][col1 - 1] = "x"

        print("+---+---+---+")
        for i in range(3):
            for j in range(3):
                print("| " + tic[i][j].upper(), end=" ")
            print("|")
            print("+---+---+---+")

        print("Player 2: O")
        row2 = int(input("Type the number of row you would like to choose: "))
        while row2 < 1 or row2 > 3:
            row2 = int(input("The number of row must be between 1 and 3: "))

        col2 = int(input("Type the number of column you would like to choose: "))
        while col2 < 1 or col2 > 3:
            col2 = int(input("The number of col must be between 1 and 3: "))

        while tic[row2 - 1][col2 - 1] != " ":
            print("This box has already a value. Please choose another one.")
            row2 = int(input("Type the number of row you would like to choose: "))
            col2 = int(input("Type the number of column you would like to choose: "))

        tic[row2 - 1][col2 - 1] = "o"

        print("+---+---+---+")
        for i in range(3):
            for j in range(3):
                print("| " + tic[i][j].upper(), end=" ")
            print("|")
            print("+---+---+---+")
