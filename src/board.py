import numpy as np
import src.block as bl







class Board:
    def __init__(self, board):
        self.board = board
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






if __name__ == "__main__":
    b = np.zeros((8, 8), dtype=int)

    newBlock = bl.Block(2)
    newBoard = Board(b)
    newBoard.add_block(newBlock, [-1, 3])

    print(newBoard.board)