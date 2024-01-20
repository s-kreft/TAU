import numpy as np
import random
import keyboard


rows = 0
columns = 0
board = []
playerPositionX = 0
playerPositionY = 0
endPositionX = 5
endPositionY = 0

def Game():
    PrepareGame()
    Gameplay()

def PrepareGame():
    GenerateBoard()
    ObstaclesGenerator()
    StartField()
    EndField()
    ShowBoard()
   # MoveRight()

def Gameplay():
    while not (playerPositionX == endPositionX and playerPositionY == endPositionY):
            GameMovements()
    else:            
        print("You win!")

    # while not (playerPositionX == endPositionX and playerPositionY == endPositionY):
    #     if keyboard.is_pressed('q'):
    #         break
    #     else:  
    #         GameMovements()
    # else:            
    #     print("You win!")

    
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
    obstaclesNumber = 10
    x = 0
    while x <= obstaclesNumber:
        randomRow = random.randint(0,4)
        randomColumn = random.randint(0,4)
        board[randomRow][randomColumn] = '@'
        x +=1

def ShowBoard():
    print(board)


def GameMovements():
    global playerPositionX
    global playerPositionY
    global endPositionX
    global endPositionY
    global board

    key = keyboard.wait()
    if key == 'q':
        board[playerPositionY][playerPositionX] = '#'
        playerPositionX += 1
        board[playerPositionY][playerPositionX] = 'P'
        print(board)
        print("prawa szczauka")

    if keyboard.is_pressed('left'):
        board[playerPositionY][playerPositionX] = '#'
        playerPositionX -= 1
        board[playerPositionY][playerPositionX] = 'P'
        print(board)
        print("lewa szczauka")
        

    if keyboard.is_pressed('up'):
        board[playerPositionY][playerPositionX] = '#'
        playerPositionY -= 1
        board[playerPositionY][playerPositionX] = 'P'
        print(board)
        print("gorna szczauka")
        

    if keyboard.is_pressed('down'):
        board[playerPositionY][playerPositionX] = '#'
        playerPositionY += 1
        board[playerPositionY][playerPositionX] = 'P'
        print(board)
        print("dolna szczauka")
                    


Game()
#print(board)






        