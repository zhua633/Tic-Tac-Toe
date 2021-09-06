"""
Tic Tac Toe Player
"""

import math
import copy
import pygame
from globalvar import *
dis, turn


X = "X"
O = "O"
EMPTY = None
best_move=()

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
    #Return the number of non zero elements
    elements=empty(board)

    #if the board is empty, X gets the first move. Or if there is even number on board.
    if (elements %2)==0:
        turn="X"
    else:
        turn="O"

    return turn

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    act = set()

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == EMPTY:
                act.add((i, j))

    print("act is this: ")
    print(act)
    return act



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    If the grid is not already occupied, draw x or o at action.
    """
    #make a deep copy of the board
    state=copy.deepcopy(board)
    i=action[0]
    j=action[1]

    turn=player(state)

    if ((state[i][j] != "X") and (state[i][j] != "O")):
        print("=turn returns this: ")
        print(turn)
        if (turn=="X"):
            state[i][j]=turn
            turn=O
        elif (turn=="O"):
            state[i][j]=turn
            turn=X
            
    return state

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
        [board[2][0], board[1][1], board[0][2]]
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

    if terminal(board):
        return None
    
    
    if player(board)==X:
        max=max_val(board)
        print("max value is")
        print(max)
    elif player(board)==O:
        min=min_val(board)
        print("min value is")
        print(min)
    
    #(3,3) is the default to get stored actions
    best=get_best((3,3))
    print(best)

    return best

def max_val(state):
    v=float('-inf')
    if terminal(state):
        return utility(state)
    for action in actions(state):
        min=min_val(result(state,action))
        print("min is this")
        print(min)
        if min==None:
            return v
        v=max(v,min)
        print("v is this:")
        print(v)
        if v==1:
            get_best(action)
            print("returning v")
            return v


def min_val(state):
    v=float('inf')
    if terminal(state):
        return utility(state)
    for action in actions(state):
        max=max_val(result(state,action))
        if max==None:
            return v
        v=min(v,max)        
        print("min v is this:")
        print(v)
        if max==-1:
            get_best(action)
            return v

def get_best(action):
    if action !=(3,3):
        global best_move
        best_move=action 
    return best_move