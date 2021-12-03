from os import devnull
import numpy as np
file_name = 'input.txt'
with open(file=file_name) as f:
    data = f.readlines()
data = list( map(  lambda line: line.strip('\n'), data) )

Nwords = len(data)
Lwords = len(data[0])
codes = np.zeros([Nwords,Lwords])
for i in range(Nwords):
    codes[i] = np.array( list(data[i]), dtype=int )

sum_codes = codes.sum(axis=0)
mask = sum_codes > Nwords / 2

bin_gamma = np.array(mask, dtype=int)
bin_epsilon = np.array( np.logical_not(mask), dtype=int)

gamma = 0
for i, val in enumerate( np.flip(bin_gamma) ):
    gamma = gamma + val*2**i

epsilon = 0
for i, val in enumerate(np.flip(bin_epsilon)):
    epsilon = epsilon + val*2**i

print( gamma, epsilon )
print( gamma*epsilon )

