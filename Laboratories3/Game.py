import numpy as np
import random
import keyboard


rows = 0
columns = 0
board = []
playerPositionX = 0
playerPositionY = 0
endPositionX = 4
endPositionY = 0
end = False

def Game():
    PrepareGame()
    Gameplay()

def PrepareGame():
    GenerateBoard()
    ObstaclesGenerator()
    StartField()
    EndField()
    ShowBoard()
    
def GenerateBoard():
    global rows
    global columns
    global board
    rows = 5
    columns  = 5
    board = np.chararray((rows,columns))
    board[:] = '='

def StartField():
    global playerPositionY
    randomField = random.randint(0,4)
    board[randomField][0] = 'S'
    playerPositionY = randomField

def EndField():
    global endPositionY
    randomField = random.randint(0,4)
    board[randomField][4] = 'E'
    endPositionY = randomField

def ObstaclesGenerator():
    obstaclesNumber = 8
    x = 0
    while x <= obstaclesNumber:
        randomRow = random.randint(0,4)
        randomColumn = random.randint(0,4)
        board[randomRow][randomColumn] = '@'
        x +=1

def ShowBoard():
    print(board)

def Gameplay():
    global end
    keyboard.on_press(GameMovements)
    while not (playerPositionX == endPositionX and playerPositionY == endPositionY):
        i = 0
    else:
         print("You Win!")

def GameMovements(k: keyboard.KeyboardEvent):
    global playerPositionX
    global playerPositionY
    global endPositionX
    global endPositionY
    global board

    if k.name == 'right':
        if (playerPositionX + 1 > 4 or playerPositionX + 1 < 0):
                print("Forbidden Move!")
        else:
            if board[playerPositionY][playerPositionX + 1] == b'@':
                print("Obstacle!")
            else:
                board[playerPositionY][playerPositionX] = '#'
                playerPositionX += 1
                board[playerPositionY][playerPositionX] = 'P'
                print("")
                print(board)
                print("Movement Right")

    if k.name == 'left':
        if (playerPositionX - 1 > 4 or playerPositionX - 1 < 0):
                print("Forbidden Move!")
        else:
            if board[playerPositionY][playerPositionX - 1] == b'@':
                print('Obstacle!')
            else:
                board[playerPositionY][playerPositionX] = '#'
                playerPositionX -= 1
                board[playerPositionY][playerPositionX] = 'P'
                print("")
                print(board)
                print("Movement Left")

    if k.name == 'up':
        if (playerPositionY - 1 > 4 or playerPositionY - 1 < 0):
                print("Forbidden Move!")
        else:
            if board[playerPositionY - 1][playerPositionX] == b'@':
                print('Obstacle!')
            else:
                board[playerPositionY][playerPositionX] = '#'
                playerPositionY -= 1
                board[playerPositionY][playerPositionX] = 'P'
                print("")
                print(board)
                print("Movement Up")
        
    if k.name == 'down':
        if (playerPositionY + 1 > 4 or playerPositionY + 1 < 0):
                    print("Forbidden Move!")
        else:
            if board[playerPositionY + 1][playerPositionX] == b'@':
                print('Obstacle!')
            else:
                board[playerPositionY][playerPositionX] = '#'
                playerPositionY += 1
                board[playerPositionY][playerPositionX] = 'P'
                print("")
                print(board)
                print("Movement Down")

#Game()







        