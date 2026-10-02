import src.board as bo
import src.block as bl
import numpy as np


class TerminalGame:
    def __init__(self, size):
        self.board = bo.Board(np.zeros((size, size), dtype=int))
        self.b1 = bl.Block(np.random.randint(18))
        self.b2 = bl.Block(np.random.randint(18))
        self.b3 = bl.Block(np.random.randint(18))

    #collect block choice and location from player playing from terminal
    def make_terminal_move(self): 
        match input(f"choose block: b1: {self.b1.arr} \n b2:{self.b2.arr} \n b3: {self.b3.arr} \n"):
            case "b1":
                block_choice = self.b1
            case "b2":
                block_choice = self.b2
            case "b3":
                block_choice = self.b3
        block_placement = np.fromstring(input(f"enter location with form [row, column]...{self.board.board}"), sep=",", dtype = int)
            #TODO fix formatting of block placement 
        self.board.add_block(block_choice, block_placement)
        block_choice = None

    def check_block_pool(self):
        if not (self.b1 or self.b2 or self.b3):
            self.b1 = bl.Block(np.random.randint(18))
            self.b2 = bl.Block(np.random.randint(18))
            self.b3 = bl.Block(np.random.randint(18))

    def check_game_over(self):
        pass




def runTheGame():
    print("Running the game right now... Be patient!")
    G = TerminalGame(8)
    G.make_terminal_move()
    G.check_block_pool
    print(G.board.board)










if __name__ == "__main__":
    runTheGame()