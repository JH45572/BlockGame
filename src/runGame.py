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
        fail_flag = False
        match input(f"choose block: \nb1: \n{self.b1.arr if self.b1 else "Empty"} \n b2: \n{self.b2.arr if self.b2 else "Empty"} \n b3: \n{self.b3.arr if self.b3 else "Empty"} \n"):
            case "b1":
                if self.b1:
                    block_choice = self.b1
                    block_placement = np.fromstring(input(f"enter location with form \"row, column\"...\n{self.board.board}"), sep=",", dtype = int)
                    if self.board.add_block(block_choice, block_placement): #only nullifies block in pool if block is successfully added
                        self.b1 = None
                    else:
                        fail_flag = True
                        print("invalid")
                else:
                    fail_flag = True
                    print("invalid")
            case "b2":
                if self.b2:
                    block_choice = self.b2
                    block_placement = np.fromstring(input(f"enter location with form \"row, column\"...\n{self.board.board}"), sep=",", dtype = int)
                    if self.board.add_block(block_choice, block_placement): #only nullifies block in pool if block is successfully added
                        self.b2 = None
                    else:
                        fail_flag = True
                        print("invalid")
                else:
                    fail_flag = True
                    print("invalid")
            case "b3":
                if self.b3:
                    block_choice = self.b3
                    block_placement = np.fromstring(input(f"enter location with form \"row, column\"...\n{self.board.board}"), sep=",", dtype = int)
                    if self.board.add_block(block_choice, block_placement): #only nullifies block in pool if block is successfully added
                        self.b3 = None
                    else:
                        fail_flag = True
                        print("invalid")
                else:
                    fail_flag = True
                    print("invalid")
            case _: 
                print("Must choose in form b1, b2, or b3")
        return not fail_flag

    #Refresh b1, b2, b3 if all are exhausted 
    def check_block_pool(self): 
        if not (self.b1 or self.b2 or self.b3):
            self.b1 = bl.Block(np.random.randint(18))
            self.b2 = bl.Block(np.random.randint(18))
            self.b3 = bl.Block(np.random.randint(18))

    def check_game_over(self):
        failureb1 = True
        failureb2 = True
        failureb3 = True
        if(self.b1):
            if(self.board.check_block_placeability(self.b1)):
                failureb1 = False
        if(self.b2):
            if(self.board.check_block_placeability(self.b2)):
                failureb2 = False
        if(self.b3):
            if(self.board.check_block_placeability(self.b3)):
                failureb3 = False
        #Check if no existing blocks are placeable        
        if (self.b1 or self.b2 or self.b3) and (failureb1 and failureb2 and failureb3): 
            print("GAME OVER!")
            return True
        else:
            return False



def runTheGame():
    G = TerminalGame(BOARD_SIZE)
    numTurns = 0
    while(not G.check_game_over()): #TODO get game over to trigger when it should
        #print(f"After checking if game over: \n{G.board.board}")

        G.check_block_pool()
        #print(f"After checking block pool: \n{G.board.board}")       

        if G.make_terminal_move(): 
            #print(f"After making terminal move: \n{G.board.board}")

            G.board.update_board()
            print(f"After updating board: \n{G.board.board}")

            numTurns += 1
            print(f"Turn number: {numTurns}")
    print("\n\n\nThank you for Playing!\n\n\n")










if __name__ == "__main__":
    runTheGame()