import numpy as np
from config import BOARD_SIZE
import src.block as bl




class Board:
    def __init__(self, board):
        self.board = board

    def deep_copy(self):
        return Board(self.board.copy())
    
    #Adds a Block (type Block) at loc (type array e.g. [row, column]) on self.board
    #Returns False if adding the block fails (i.e. location out of bounds or invalid)
    def add_block(self, Block, loc):
        sh = Block.arr.shape
        fail_flag = False
        if(Block == None):
            fail_flag = True
        if(Block.test_loc(loc)):
            newarr = self.board[loc[0]:sh[0]+loc[0], loc[1]:sh[1]+loc[1]] + Block.arr
            for x in np.nditer(newarr):
                if (x > 1):
                    fail_flag = True
            if fail_flag == False:
                self.board[loc[0]:sh[0]+loc[0], loc[1]:sh[1]+loc[1]] = newarr
        else:
            fail_flag = True
        return not fail_flag

    def check_block_placeability(self, block):
        placeability = False
        for x in range(len(self.board)):
            for y in range(len(self.board)):
                boardCopy = self.deep_copy()
                if(boardCopy.add_block(block, [x, y])):
                    placeability = True
        return placeability

    #Clears all full rows/columns
    def update_board(self):       
        filter_column = np.all(self.board, axis = 0)
        filter_row = np.all(self.board, axis = 1)
        newBoard = self.board.copy()
        newBoard[filter_row, :] = 0
        newBoard[:, filter_column] = 0
        self.board = newBoard

