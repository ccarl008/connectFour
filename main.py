import random
print("-------------------------------------------------")
print(r"""
----------------------------------------------------------
                                          __   __
  ____                            _      |  | |  |
 / ___|___  _ __  _ __   ___  ___| |_    |  | |  |__
| |   / _ \| '_ \| '_ \ / _ \/ __| __|   |____    __|
| |__| (_) | | | | | | |  __/ (__| |_         |  |
 \____\___/|_| |_|_| |_|\___|\___|\__|        |__|
----------------------------------------------------------
""")

possibleLetters = ['A', 'B', 'C','D','E','F', 'G' ]
gameBoard = [["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""]]

rows = 6
cols = 7

def printGameBoard():
    print("\n     A    B    C    D    E    F    G  ", end = "")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(x, " |", end = "")
        for y in range(cols):
            if(gameBoard[x][y] == "🔵"):
                print("",gameBoard[x][y], end = " |")
            elif (gameBoard[x][y] == "🔴"):
                print("",gameBoard[x][y], end = " |")
            else:
                print(" ",gameBoard[x][y], end = "  |")
    print("\n   +----+----+----+----+----+----+----+")

def modifyArray(spacePicked, turn):
    gameBoard[spacePicked[0]][spacePicked[1]] = turn

def checkForWinner(chip):
    # Check horizontal (row) wins
    for row in range(rows):
        for col in range(cols - 3):
            if (gameBoard[row][col] == chip and 
                gameBoard[row][col+1] == chip and 
                gameBoard[row][col+2] == chip and 
                gameBoard[row][col+3] == chip):
                print("\nGame over", chip, "wins! Thank you for playing!")
                return True
    
    # Check vertical (column) wins
    for col in range(cols):
        for row in range(rows - 3):
            if (gameBoard[row][col] == chip and 
                gameBoard[row+1][col] == chip and 
                gameBoard[row+2][col] == chip and 
                gameBoard[row+3][col] == chip):
                print("\nGame over", chip, "wins! Thank you for playing")
                return True

    # Check diagonal (top-left to bottom-right)
    for row in range(rows - 3):
        for col in range(cols - 3):
            if (gameBoard[row][col] == chip and 
                gameBoard[row+1][col+1] == chip and 
                gameBoard[row+2][col+2] == chip and 
                gameBoard[row+3][col+3] == chip):
                print("\nGame over", chip, "wins! Thank you for playing")
                return True

    # Check diagonal (top-right to bottom-left)
    for row in range(rows - 3):
        for col in range(3, cols):
            if (gameBoard[row][col] == chip and 
                gameBoard[row+1][col-1] == chip and 
                gameBoard[row+2][col-2] == chip and 
                gameBoard[row+3][col-3] == chip):
                print("\nGame over", chip, "wins! Thank you for playing")
                return True
    return False

def coordinateParser(inputString):
    coordinate = [None] * 2
    if inputString[0].upper() == "A":
        coordinate[1] = 0
    elif inputString[0].upper() == "B":
        coordinate[1] = 1
    elif inputString[0].upper() == "C":
        coordinate[1] = 2 
    elif inputString[0].upper() == "D":
        coordinate[1] = 3 
    elif inputString[0].upper() == "E":
        coordinate[1] = 4 
    elif inputString[0].upper() == "F":
        coordinate[1] = 5  
    elif inputString[0].upper() == "G":
        coordinate[1] = 6
    else:
        print("Invalid Column")
        return None
    
    try:
        row = int(inputString[1])
        if row < 0 or row >= rows:
            print("Invalid Row")
            return None
        coordinate[0] = row
        return coordinate
    except:
        print("Invalid Coordinate")
        return None

def isSpaceAvail(intendedCoordinate):
    if (gameBoard[intendedCoordinate[0]][intendedCoordinate[1]] == '🔴'):
        return False
    elif (gameBoard[intendedCoordinate[0]][intendedCoordinate[1]] == '🔵'):
        return False
    else:
        #print("Space is available")
        return True

def gravityChecker(intendedCoordinate):
    # Caluclate space below
    spaceBelow = [None] * 2
    spaceBelow[0] = intendedCoordinate[0] + 1
    spaceBelow[1] = intendedCoordinate[1]

    # Is coordinate at ground level
    if(spaceBelow[0] == 6):
        #print("Gravity satisfied")
        return True
    
    # Check if there is a token below
    if(isSpaceAvail(spaceBelow) == False):
        return True
    return False

turnCounter = 0
while True:
    if(turnCounter % 2 == 0):
        printGameBoard()
        while True:
            spacePicked = input("\nChoose a space: ")
            coordinate = coordinateParser(spacePicked)
            try:
                # Check if space is avail
                if(isSpaceAvail(coordinate) and gravityChecker(coordinate)):
                    modifyArray(coordinate, '🔵')
                    break
                else:
                    print("Not a valid coordinate")
            except:
                print("Please try again.")
        winner = checkForWinner('🔵')
        turnCounter += 1
    # It's the computers turn
    else:
        while True:
            cpuChoice = [random.choice(possibleLetters), random.randint(0,5)]
            cpuCoordinate = coordinateParser(cpuChoice)
            if(isSpaceAvail(cpuCoordinate) and gravityChecker(cpuCoordinate)):
                modifyArray(cpuCoordinate, '🔴')
                break
        turnCounter += 1
        winner = checkForWinner('🔴')
    if(winner):
        printGameBoard
        break