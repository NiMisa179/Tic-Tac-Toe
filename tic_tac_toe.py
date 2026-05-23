print("Tic Tac Toe!")
ans = input("S T A R T: Y/N?: ")
tic = [" " for i in range(9)]
while ans.upper() == "Y":

    for i in range(9 // 2):

        row1 = int(input("Type the number of row you would like to choose: "))
        while row1 < 1 or row1 > 3:
            row1 = int(input("The number of row must be between 1 and 3: "))

        col1 = int(input("Type the number of column you would like to choose: "))
        while col1 < 1 or col1 > 3:
            col1 = int(input("The number of col must be between 1 and 3: "))

        pass

        print("+---+---+---+")
        print("| " + tic[0].upper() + " | " + tic[1].upper() + " | " + tic[2].upper() + " |")
        print("+---+---+---+")
        print("| " + tic[3].upper() + " | " + tic[4].upper() + " | " + tic[5].upper() + " |")
        print("+---+---+---+")
        print("| " + tic[6].upper() + " | " + tic[7].upper() + " | " + tic[8].upper() + " |")
        print("+---+---+---+")


