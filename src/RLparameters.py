import numpy as np
import runGUIsmall as rg
import block as bl
import board as bo


#NOTE: not configurable to any BOARD_SIZE other than 3

#Reward values to be used to train Q-table
REWARD_INVALID = -100
REWARD_GAME_OVER = -50
REWARD_NONE_CLEARED = 5
REWARD_LINE_CLEARED = 10

Q_table = {}



class AiGame():
    def __init__(self, root, Q_table):
        self.game = rg.BlockPuzzleGUI(root, True)
        self.Q_table = Q_table

    def stringify_state(self):
        board = self.game.board
        block_pool = self.game.blocks
        state_string = ""
        #first 9 characters specify board state:
        for char in np.nditer(board): 
            state_string += char
        #last 3 characters specify block pool; "n" if null; else index of block in rg.small_blocks (0 to length-1)
        for block in block_pool:
            state_string += map_block_to_idx(block)
        return state_string
    
    #add a block from pool to board
    def take_action(self, action_index): #action_index can be 0 to 26; 
        raw_loc = 0
        block_pool_idx = 0
        if 0 <= action_index and action_index <= 8:
            raw_loc = action_index
            block_pool_idx = 0
        elif 9 <= action_index and action_index <= 17:
            raw_loc = action_index - 9
            block_pool_idx = 1
        elif 18 <= action_index and action_index <= 26:
            raw_loc = action_index - 18
            block_pool_idx = 2
        else:
            print("invalid action index")
            return False
        loc = [raw_loc//3, raw_loc%3] #converts raw_loc to loc usable in bo.add_block()
        if(self.game.board.add_block(self.game.blocks[block_pool_idx], loc)):
            return True #block added successfully
        else:
            return False #invalid move


    def update_Q_table(self, state, action_index):#TODO implement proper algorithm
        current_Q_val = self.Q_table[state][action_index] #current Q-val for state-action pair
        new_Q_val = Bellman_eq(current_Q_val)
        self.Q_table.update({state: self.Q_table[state][action_index]}) 

def Bellman_eq(): #TODO 
    pass

#finds the index of current block in rg.small_blocks
def map_block_to_idx(block): #TODO verify that this works
    array = block.arr
    if array == None:
        return "n"
    for idx in range(len(rg.small_blocks)):
        if bl.Block(rg.small_blocks[idx]).arr == array:
            return idx



