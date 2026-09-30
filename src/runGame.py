import src.board as bo
import src.block as bl
import numpy as np


def runTheGame():
    print("Running the game right now... Be patient!")
    b = np.zeros((8, 8), dtype=int)

    newBlock = bl.Block(10)
    newBoard = bo.Board(b)
    newBoard.add_block(newBlock, [0, 4])
    print(newBoard.board)
    newBlock = bl.Block(12)
    newBoard.add_block(newBlock, [0, 3])
    print(newBoard.board)










if __name__ == "__main__":
    runTheGame()