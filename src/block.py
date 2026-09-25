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

b1 = Block(2)

print(b1.arr)
