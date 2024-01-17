import numpy as np
import random


rows = 0
columns = 0
board = []

def PrepareGame():
    GenerateBoard()
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
    randomField = random.randint(0,4)
    board[randomField][0] = 'S'

def EndField():
    randomField = random.randint(0,4)
    board[randomField][4] = 'E'

def ShowBoard():
    print(board)

PrepareGame()






        