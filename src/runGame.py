import src.board as bo
import src.block as bl
import numpy as np
from config import BOARD_SIZE


class TerminalGame:
    def __init__(self, size):
        self.board = bo.Board(np.zeros((size, size), dtype=int))
        self.b1 = bl.Block(np.random.randint(18))
        self.b2 = bl.Block(np.random.randint(18))
        self.b3 = bl.Block(np.random.randint(18))

    #collect block choice and location from player playing from terminal
    def make_terminal_move(self): 
        match input(f"choose block: b1: {self.b1.arr if self.b1 else "Empty"} \n b2:{self.b2.arr if self.b2 else "Empty"} \n b3: {self.b3.arr if self.b3 else "Empty"} \n"):
            case "b1":
                if self.b1:
                    block_choice = self.b1
                    self.b1 = None
                else:
                    print("invalid")
            case "b2":
                if self.b2:
                    block_choice = self.b2
                    self.b2 = None
                else:
                    print("invalid")
            case "b3":
                if self.b3:
                    block_choice = self.b3
                    self.b3 = None
                else:
                    print("invalid")
        block_placement = np.fromstring(input(f"enter location with form [row, column]...{self.board.board}"), sep=",", dtype = int)
        self.board.add_block(block_choice, block_placement)

    #Refresh b1, b2, b3 if all are exhausted 
    def check_block_pool(self): 
        if not (self.b1 or self.b2 or self.b3):
            self.b1 = bl.Block(np.random.randint(18))
            self.b2 = bl.Block(np.random.randint(18))
            self.b3 = bl.Block(np.random.randint(18))

    def check_game_over(self):
        failureb1 = False
        failureb2 = False
        failureb3 = False
        if(self.b1):
            if(not (self.board.check_block_placeability(self.b1))):
                failureb1 = True
        if(self.b2):
            if(not (self.board.check_block_placeability(self.b2))):
                failureb2 = True
        if(self.b3):
            if( not (self.board.check_block_placeability(self.b3))):
                failureb3 = True
        #Check if no blocks are placeable        
        if (failureb1 and failureb2 and failureb3): #game over
            print("GAME OVER!")
            return True
        else:
            return False



def runTheGame():
    G = TerminalGame(BOARD_SIZE)
    numTurns = 0
    while(not G.check_game_over()):
        print(f"After checking if game over: \n{G.board.board}")

        G.check_block_pool()
        print(f"After checking block pool: \n{G.board.board}")       

        G.make_terminal_move()
        print(f"After making terminal move: \n{G.board.board}")

        G.board.update_board()
        print(f"After updating board: \n{G.board.board}")

        numTurns += 1
        print(f"Turn number: {numTurns}")
    










if __name__ == "__main__":
    runTheGame()