from ctypes import pointer
import numpy as np
with open( file='input.txt', mode='r') as f:
    positions = np.array( f.readline().split(','), dtype = int )
positions = np.expand_dims(positions, axis=1)
L = np.min(positions)
R = np.max(positions)
N = len(positions)
targets = np.tile(np.arange(L,R+1), [N, 1])
costs = np.sum( np.abs( positions - targets ), axis=0)
print(np.min(costs))