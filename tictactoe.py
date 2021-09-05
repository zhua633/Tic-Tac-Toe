"""
Tic Tac Toe Player
"""

import math
import pygame
from globalvar import *
dis, turn


X = "X"
O = "O"
EMPTY = None

# Colors
white=(255,255,255)

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
    board[i][j]=turn
    print("player is this")
    print(board[i][j])


def draw_o(board,i,j):
    centerX = j * 100 + 50
    centerY = i * 100 + 50
    pygame.draw.circle (dis, white, (centerX, centerY), 44, 2)
    board[i][j]=turn


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
            


def this_player(board):
    """
    Returns player who has the next turn on a board.
    """
    #Return the number of non zero elements
    elements=empty(board)

    #if the board is empty, X gets the first move. Or if there is even number on board.
    if (elements %2)==0:
        turn="X"
    else:
        turn="O"

    return turn

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #Return the number of non zero elements
    elements=empty(board)

    #if the board is empty, X gets the first move. Or if there is even number on board.
    if (elements %2)==0:
        turn="O"
    else:
        turn="X"

    return turn

def actions():
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    act = {(0,0),(0,1),(0,2),
            (1,0),(1,1),(1,2),
            (2,0),(2,1),(2,2)}

    #if ((board[i][j] == "X") or (board[i][j] == "O")):
    #    return act
    print(act)
    return act



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    If the grid is not already occupied, draw x or o at action.
    """
    i=action[0]
    j=action[1]

    turn=this_player(board)

    if ((board[i][j] != "X") and (board[i][j] != "O")):
        print("=turn returns this: ")
        print(turn)
        if (turn=="X"):
            draw_x(board,i,j)
        elif (turn=="O"):
            draw_o(board,i,j)
            
    turn=player(board)

    return board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    victory = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]

    if [turn,turn,turn] in victory:
        return turn
    else:
        return None

def terminal(board):
    """
    Returns True if game is over(there is a winner or the board is full), False otherwise.
    """
    isFull=empty(board)

    if winner(board) !=None or isFull==9:
        return True

    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) !=None:
        if winner(board)==X:
            return 1
        elif winner(board)==O:
            return -1
    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    return (2,2)