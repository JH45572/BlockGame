import numpy as np
import block as bl

class Board:
    def __init__(self, board):
        self.board = board
    def add_block(self, Block, loc):
        Block.arr = Block.arr + loc           #TODO resolve shape discrepancy, add location parameter
        self.board = self.board + Block.arr 

b = np.zeros((8, 8), dtype=int)

newBlock = bl.Block(2)
newBoard = Board(b)
newBoard.add_block(newBlock)

print(newBoard.board)