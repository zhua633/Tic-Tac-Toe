"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None

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
    #Return the non zero elements

    elements=empty(board)

    print("elements returns this: ")
    print(elements)

    #if the board is empty, X gets the first move. Or if there is even number on board.
    if elements==0 or (len(elements) %2)==1:
        return X
    else:
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

    return act



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
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