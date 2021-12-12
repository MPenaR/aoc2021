import numpy as np
with open(file='input.txt', mode='r') as f:
    lines = f.readlines()
energy_levels = np.array(  [ list(line.strip("\n")) for line in lines ], dtype=int)
nrows, ncols = energy_levels.shape
i = np.arange(ncols)
j = np.arange(nrows)
I, J = np.meshgrid(i,j,indexing="ij")

def flash( energy_levels, Nflashes, old_flashes = None ):
    flashes = list(zip( I[energy_levels > 9],J[energy_levels > 9]))
    for i, j in flashes:
        mask = np.less_equal( max(0,i-1), I ) & np.less_equal(I, min(i+1,nrows) ) & np.less_equal( max(0,j-1), J ) & np.less_equal(J, min(j+1,ncols) )
        energy_levels[mask] += 1
        Nflashes += 1 
    if old_flashes is not None:
        flashes += old_flashes
    for i, j in flashes:
        energy_levels[ i, j ] = 0

    if np.any( energy_levels > 9 ):
        energy_levels, Nflashes = flash(energy_levels, Nflashes, flashes)
        return [energy_levels, Nflashes]
    else:
        return [energy_levels, Nflashes]

Nsteps = 100
Nflashes = 0
for step in range(Nsteps):
    energy_levels +=1
    print('step {}'.format(step)) 
    energy_levels, Nflashes = flash(energy_levels, Nflashes)

print(energy_levels)
print(Nflashes)