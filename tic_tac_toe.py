print("Tic Tac Toe!")
ans = input("S T A R T: Y/N?: ")

while ans.upper() == "Y":
    row1 = int(input("Type the number of row you would like to choose: "))
    while row1 < 1 or row1 > 3:
        row1 = int(input("The number of row must be between 1 and 3 "))