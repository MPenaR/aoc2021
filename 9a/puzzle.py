import numpy as np
with open(file='input.txt', mode='r') as f:
    lines = f.readlines()
height = np.array( [ list(line.strip('\n')) for line in lines ], dtype=int)
nrows, ncols = np.shape(height)
gradx = height[:,1:] - height[:,:-1]
grady = height[:-1,:] - height[1:,:]
right = np.concatenate( [ gradx > 0, np.ones([nrows,1], dtype=bool) ], axis = 1)
left  = np.concatenate( [ np.ones([nrows,1], dtype=bool), gradx < 0 ], axis = 1) 
up    = np.concatenate( [ np.ones([1,ncols], dtype=bool), grady > 0 ], axis = 0)
down  = np.concatenate( [ grady < 0, np.ones([1,ncols], dtype=bool) ], axis = 0)
print( (height[ left & right & up & down ]+1).sum() )