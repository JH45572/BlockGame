import numpy as np
from config import BOARD_SIZE



#code of each block
def num_to_type(num):
    match num:
        case 0:
            return np.ones((2, 2), dtype=int) #small square block
        case 1:
            return np.ones((3, 3), dtype=int) #large square block
        case 2:
            return np.array([[1, 0, 0],
                          [1, 0, 0],
                          [1, 1, 1]])
        case 3:
            return np.array([[1, 1, 1],
                          [0, 0, 1],
                          [0, 0, 1]])
        case 4:
            return np.array([[1, 1, 1],
                          [1, 0, 0],
                          [1, 0, 0]])
        case 5:
            return np.array([[0, 0, 1],
                          [0, 0, 1],
                          [1, 1, 1]])
        case 6:
            return np.array([[1]])
        case 7:
            return np.array([[1, 1]])
        case 8:
            return np.array([[1, 1, 1]])
        case 9:
            return np.array([[1, 1, 1, 1]])
        case 10:
            return np.array([[1, 1, 1, 1, 1]])
        case 11:
            return np.array([[1, 0],
                          [1, 1]])
        case 12:
            return np.array([[1, 1],
                          [0, 1]])
        case 13:
            return np.array([[1, 1],
                          [1, 0]])
        case 14:
            return np.array([[0, 1],
                          [1, 1]])
        case 15:
            return np.array([[1],
                          [1]])
        case 16:
            return np.array([[1],
                          [1],
                          [1]])
        case 17:
            return np.array([[1],
                          [1],
                          [1],
                          [1]])
        case 18:
            return np.array([[1],
                          [1],
                          [1],
                          [1],
                          [1]])


        
class Block:
    def __init__(self, typeNum):
        self.arr = num_to_type(typeNum)

    #returns True if block can fit on board when loc is upper left coordinate    
    def test_loc(self, loc):
        if (loc[0]+self.arr.shape[0] > BOARD_SIZE) or (loc[1]+self.arr.shape[1] > BOARD_SIZE) or (loc[0] < 0) or (loc[1] < 0):
            return False
        else:
            return True




