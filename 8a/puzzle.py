import numpy as np
with open( file = 'input.txt', mode='r') as f:
    lines = [ line.split(' | ') for line in f.readlines()]

bases = [ line[0].split(' ') for line in lines ]
codes = np.array([ line[1].strip('\n').split(' ') for line in lines ])

digit_n_segments = [6, 2, 5, 4, 5, 6, 3, 7, 6]

known_lengths = np.array([2,3,4,7])

nplen = np.vectorize( lambda a: len(a))


print(np.sum(np.isin( nplen(codes) , known_lengths)))
