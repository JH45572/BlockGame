import src.board as bo
import src.block as bl
import numpy as np




def player_move(board, currblocks): #TODO finish
    block_choice = input(f"choose block: {currblocks}")
    block_choice.used = True
    block_placement = input(f"enter location with form [row, column]...{board}")
    board.add_block(block_choice, block_placement)

def runTheGame():
    print("Running the game right now... Be patient!")
    b = np.zeros((8, 8), dtype=int)

    newBoard = bo.Board(b)
    newBoard.add_block(bl.Block(18), [0, 0])
    newBoard.add_block(bl.Block(2), [5, 1])
    newBoard.add_block(bl.Block(2), [5, 4])
    newBoard.add_block(bl.Block(18), [4, 7])
    newBoard.add_block(bl.Block(18), [4, 0])
    print(newBoard.board)
    newBoard.update_board()
    print(newBoard.board)










if __name__ == "__main__":
    runTheGame()