import numpy as np
from config import BOARD_SIZE

def num_to_type(num):
    match num:
        case 1:
            return np.ones((2, 2), dtype=int) #small square block
        case 2:
            return np.ones((3, 3), dtype=int) #large square block
        case 3:
            return np.array([[1, 0, 0],
                          [1, 0, 0],
                          [1, 1, 1]])
        case 4:
            return np.array([[1, 1, 1],
                          [0, 0, 1],
                          [0, 0, 1]])
        case 5:
            return np.array([[1, 1, 1],
                          [1, 0, 0],
                          [1, 0, 0]])
        case 6:
            return np.array([[0, 0, 1],
                          [0, 0, 1],
                          [1, 1, 1]])
        case 7:
            return np.array([[1]])
        case 8:
            return np.array([[1, 1]])
        case 9:
            return np.array([[1, 1, 1]])
        case 10:
            return np.array([[1, 1, 1, 1]])
        case 11:
            return np.array([[1, 1, 1, 1, 1]])
        case 12:
            return np.array([[1, 0],
                          [1, 1]])
        case 13:
            return np.array([[1, 1],
                          [0, 1]])
        case 14:
            return np.array([[1, 1],
                          [1, 0]])
        case 15:
            return np.array([[0, 1],
                          [1, 1]])
        case 16:
            return np.array([[1],
                          [1]])
        case 17:
            return np.array([[1],
                          [1],
                          [1]])
        case 18:
            return np.array([[1],
                          [1],
                          [1],
                          [1]])
        case 19:
            return np.array([[1],
                          [1],
                          [1],
                          [1],
                          [1]])


        
class Block:
    def __init__(self, typeNum):
        self.arr = num_to_type(typeNum)
    def test_loc(self, loc):
        if (loc[0]+self.arr.shape[0] > BOARD_SIZE) or (loc[1]+self.arr.shape[1] > BOARD_SIZE) or (loc[0] < 0) or (loc[1] < 0):
            return 1
        else:
            return 0




if __name__ == "__main__":
    b1 = Block(2)
    loc = [3, 4]
    Board = np.zeros((8, 8), dtype = int)
    sh = b1.arr.shape
    if (not (b1.test_loc(loc))):
        Board[loc[0]:sh[0]+loc[0], loc[1]:sh[1]+loc[1]] += b1.arr
        print(Board)
    else:
        print("failed!")

