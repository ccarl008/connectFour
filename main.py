import random

class ConnectFour:
    def __init__(self):
        self.possibleLetters = ['A', 'B', 'C','D','E','F', 'G']
        self.gameBoard = [["","","","","","",""], 
                         ["","","","","","",""], 
                         ["","","","","","",""], 
                         ["","","","","","",""], 
                         ["","","","","","",""], 
                         ["","","","","","",""]]
        self.rows = 6
        self.cols = 7
        self.turnCounter = 0

    def print_welcome(self):
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

    def printGameBoard(self):
        print("\n     A    B    C    D    E    F    G  ", end="")
        for x in range(self.rows):
            print("\n   +----+----+----+----+----+----+----+")
            print(x, " |", end="")
            for y in range(self.cols):
                if self.gameBoard[x][y] == "🔵":
                    print("", self.gameBoard[x][y], end=" |")
                elif self.gameBoard[x][y] == "🔴":
                    print("", self.gameBoard[x][y], end=" |")
                else:
                    print(" ", self.gameBoard[x][y], end="  |")
        print("\n   +----+----+----+----+----+----+----+")

    def modifyArray(self, spacePicked, turn):
        self.gameBoard[spacePicked[0]][spacePicked[1]] = turn

    def coordinateParser(self, inputString):
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
            if row < 0 or row >= self.rows:
                print("Invalid Row")
                return None
            coordinate[0] = row
            return coordinate
        except:
            print("Invalid Coordinate")
            return None

    def isSpaceAvailable(self, intendedCoordinate):
        if (self.gameBoard[intendedCoordinate[0]][intendedCoordinate[1]] == '🔴'):
            return False
        elif (self.gameBoard[intendedCoordinate[0]][intendedCoordinate[1]] == '🔵'):
            return False
        else:
            return True

    def gravityChecker(self, intendedCoordinate):
        spaceBelow = [None] * 2
        spaceBelow[0] = intendedCoordinate[0] + 1
        spaceBelow[1] = intendedCoordinate[1]

        if spaceBelow[0] == 6:
            return True
        
        if not self.isSpaceAvailable(spaceBelow):
            return True
        return False

    def humanTurn(self):
        while True:
            spacePicked = input("\nChoose a space: ")
            coordinate = self.coordinateParser(spacePicked)
            if coordinate and self.isSpaceAvailable(coordinate) and self.gravityChecker(coordinate):
                self.modifyArray(coordinate, '🔵')
                return True
            print("Not a valid coordinate")

    def computerTurn(self):
        while True:
            cpuChoice = [random.choice(self.possibleLetters), random.randint(0,5)]
            cpuCoordinate = self.coordinateParser("".join(map(str, cpuChoice)))
            if cpuCoordinate and self.isSpaceAvailable(cpuCoordinate) and self.gravityChecker(cpuCoordinate):
                self.modifyArray(cpuCoordinate, '🔴')
                return True

    def checkForWinner(self, chip):
        # Check horizontal (left to right)
        for row in range(self.rows):
            for col in range(self.cols - 3):
                if (self.gameBoard[row][col] == chip and 
                    self.gameBoard[row][col+1] == chip and 
                    self.gameBoard[row][col+2] == chip and 
                    self.gameBoard[row][col+3] == chip):
                    print(f"\nGame over {chip} wins! Thank you for playing!")
                    return True
        
        # Check vertical (top to bottom)
        for col in range(self.cols):
            for row in range(self.rows - 3):
                if (self.gameBoard[row][col] == chip and 
                    self.gameBoard[row+1][col] == chip and 
                    self.gameBoard[row+2][col] == chip and 
                    self.gameBoard[row+3][col] == chip):
                    print(f"\nGame over {chip} wins! Thank you for playing")
                    return True

        # Check diagonal (top-left to bottom-right)
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if (self.gameBoard[row][col] == chip and 
                    self.gameBoard[row+1][col+1] == chip and 
                    self.gameBoard[row+2][col+2] == chip and 
                    self.gameBoard[row+3][col+3] == chip):
                    print(f"\nGame over {chip} wins! Thank you for playing")
                    return True

        # Check diagonal (top-right to bottom-left)
        for row in range(self.rows - 3):
            for col in range(3, self.cols):
                if (self.gameBoard[row][col] == chip and 
                    self.gameBoard[row+1][col-1] == chip and 
                    self.gameBoard[row+2][col-2] == chip and 
                    self.gameBoard[row+3][col-3] == chip):
                    print(f"\nGame over {chip} wins! Thank you for playing")
                    return True
        return False

    def play(self):
            self.print_welcome()
            
            while True:
                self.printGameBoard()
                
                if self.turnCounter % 2 == 0:
                    self.humanTurn()
                    winner = self.checkForWinner('🔵')
                else:
                    self.computerTurn()
                    winner = self.checkForWinner('🔴')
                
                self.turnCounter += 1
                
                if winner:
                    self.printGameBoard()
                    break


if __name__ == "__main__":
    game = ConnectFour()
    game.play()