import numpy as np
import runGUIsmall as rg



#Reward values to be used to train Q-table
REWARD_INVALID = -100
REWARD_GAME_OVER = -50
REWARD_NONE_CLEARED = 5
REWARD_LINE_CLEARED = 10

Q_table = {}



class state():
    def __init__(self):
        self.rg.BlockPuzzleGUI

def get_state_reward(state):
    pass