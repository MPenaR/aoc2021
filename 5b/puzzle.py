import numpy as np

with open(file='input.txt',mode='r') as f:
    lines = f.readlines()

p = np.array( [ [ segment[0].split(','), segment[1].split(',') ]  for segment in list( map( lambda line : line.split(' -> '), lines ) ) ], dtype=int)

L = np.max(p)
segments = np.zeros([L+1, L+1], dtype=int)

for a, b in p:
    v = b - a
    if any(v == 0): # vertical/horizontal lines
        #steps = abs(v[v!=0])[0]
        steps = int(np.linalg.norm(v))
        idx = np.array([ a + i*v/steps for i in range(steps+1)], dtype=int)
    else:
        steps = abs(v[0])
        idx = np.array([ a + i*v/steps for i in range(steps+1)], dtype=int)

    segments[ idx[:,0], idx[:,1] ] = segments[ idx[:,0], idx[:,1] ] + 1

print(np.sum(segments>1))
#import matplotlib.pyplot as plt
#plt.imshow(segments.transpose(), cmap='hot')
#plt.show() 