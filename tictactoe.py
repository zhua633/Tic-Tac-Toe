"""
Tic Tac Toe Player
"""

import math
import copy
import pygame



X = "X"
O = "O"
EMPTY = None

turn="X"

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

    return act



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    If the grid is not already occupied, draw x or o at action.
    """
    #make a deep copy of the board
    state=copy.deepcopy(board)

    if action not in actions(board):
        raise Exception("Invalid action")
    
    i,j=action

    turn=player(state)

    if ((state[i][j] != "X") and (state[i][j] != "O")):
        state[i][j]=turn
        if (turn=="X"):
            turn=O
        elif (turn=="O"):
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

    if [X,X,X] in victory:
        return X
    elif [O,O,O] in victory:
        return O
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
        return max_val(board,-math.inf,math.inf)[1]

    else:
        return min_val(board,-math.inf,math.inf)[1]

def max_val(state,alpha,beta):
    best_move=()
    if terminal(state):
        return utility(state),best_move
    else:
        v= -math.inf
        for action in actions(state):
            test=min_val(result(state,action),alpha,beta)[0]
            if test>v:
                v=test
                best_move=action 
            alpha=max(alpha,v)
            if (beta<=alpha):
                break
        return v, best_move


def min_val(state,alpha,beta):
    best_move=()
    if terminal(state):
        return utility(state),best_move
    else:
        v=math.inf
        for action in actions(state):
            test=max_val(result(state,action),alpha,beta)[0]
            if test<v:
                v=test
                best_move=action 
            beta=min(beta,v)
            if beta<=alpha:
                break
        return v, best_move

