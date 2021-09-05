"""
Tic Tac Toe Player
"""

import math
import pygame
from globalvar import *
dis


X = "X"
O = "O"
EMPTY = None

# Colors
white=(255,255,255)
turn="X"


def empty(board):
    """
    Return the number of non zero terms on the board
    """
    columns=3
    rows=3
    elements=0
    
    for j in range(columns):
        for i in range(rows):
            if board[i][j]!=EMPTY:
                elements+=1

    return elements

def draw_x(board,i,j):
    centerX = j * 80 + 180+40
    centerY = i * 80 + 80+40
    pygame.draw.line (dis, white, (centerX - 22, centerY - 22),
        (centerX + 22, centerY + 22), 2)

    pygame.draw.line (dis, white, (centerX + 22, centerY - 22),
        (centerX - 22, centerY + 22), 2)
    board[i][j]=player
    print("player is this")
    print(player)


def draw_o(board,i,j):
    centerX = j * 100 + 50
    centerY = i * 100 + 50
    pygame.draw.circle (dis, white, (centerX, centerY), 44, 2)
    board[i][j]=player


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
            


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #Return the non zero elements

    elements=empty(board)

    #print("elements returns this: ")
    #print(elements)

    #if the board is empty, X gets the first move. Or if there is even number on board.
    if elements==0 or (len(elements) %2)==1:
        player="X"
        return X
    else:
        player="O"
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    act = {(0,0),(0,1),(0,2),
            (1,0),(1,1),(1,2),
            (2,0),(2,1),(2,2)}

    #if ((board[i][j] == "X") or (board[i][j] == "O")):
    #    return act

    return act[1]



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    If the grid is not already occupied, draw x or o at action.
    """
    i=action[0]
    j=action[1]


    if ((board[i][j] != "X") and (board[i][j] != "O")):
        print("=turn returns this: ")
        print(turn)
        if (turn=="X"):
            draw_x(board,i,j)
        elif (turn=="O"):
            draw_o(board,i,j)
    return board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    return X

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    return True