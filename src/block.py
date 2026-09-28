import numpy as np

def num_to_type(num):
    match num:
        case 1:
            return np.ones((2, 2), dtype=int) #small square block
        case 2:
            return np.ones((3, 3), dtype=int) #large square block

class Block:
    def __init__(self, typeNum):
        self.arr = num_to_type(typeNum)
    def test_loc(self, loc):
        if (loc[0]+self.arr.shape[0] > 8) or (loc[1]+self.arr.shape[1] > 8) or (loc[0] < 0) or (loc[1] < 0):
            return 1
        else:
            return 0

b1 = Block(2)
loc = [3, 4]
Board = np.zeros((8, 8), dtype = int)
sh = b1.arr.shape
if (not (b1.test_loc(loc))):
    Board[loc[0]:sh[0]+loc[0], loc[1]:sh[1]+loc[1]] += b1.arr
    print(Board)
else:
    print("failed!")

