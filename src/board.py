import numpy as np
from config import BOARD_SIZE
import src.block as bl




class Board:
    def __init__(self, board):
        self.board = board

    #Adds a Block (type Block) at loc (type array e.g. [row, column]) on self.board
    def add_block(self, Block, loc):
        sh = Block.arr.shape
        fail_flag = 0
        if(not (Block.test_loc(loc))):
            newarr = self.board[loc[0]:sh[0]+loc[0], loc[1]:sh[1]+loc[1]] + Block.arr
            for x in np.nditer(newarr):
                if (x > 1):
                    print("invalid location")
                    fail_flag = 1
            if fail_flag == 0:
                self.board[loc[0]:sh[0]+loc[0], loc[1]:sh[1]+loc[1]] = newarr
        else:
            print("Cannot place block out of bounds")
            fail_flag = 1
        return fail_flag

    def check_block_placability(self, block):
        placability = 0
        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                newarr = self.board.copy()
                if(newarr.add_block(block, [x, y])):
                    placability = 1
        return placability



    #Clears all full rows/columns
    def update_board(self):       
        filter_column = np.all(self.board, axis = 0)
        filter_row = np.all(self.board, axis = 1)
        newBoard = self.board.copy()
        newBoard[filter_row, :] = 0
        newBoard[:, filter_column] = 0
        self.board = newBoard

