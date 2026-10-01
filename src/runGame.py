import src.board as bo
import src.block as bl
import numpy as np


class Game:
    def __init__(self, size):
        self.board = bo.Board(np.zeros((size, size), dtype=int))
        self.b1 = bl.Block(np.random.randint(18))
        self.b2 = bl.Block(np.random.randint(18))
        self.b3 = bl.Block(np.random.randint(18))

    def make_move(self): #TODO finish
        block_choice = input(f"choose block: b1: {self.b1.arr} \n b2:{self.b2.arr} \n b3: {self.b3.arr} \n")
        block_placement = np.fromstring(input(f"enter location with form [row, column]...{self.board.board}"), sep=",")
        self.board.add_block(block_choice, block_placement)
        block_choice = None



def runTheGame():
    print("Running the game right now... Be patient!")
    G = Game(8)
    G.make_move()










if __name__ == "__main__":
    runTheGame()