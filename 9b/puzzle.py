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

minima = left & right & up & down 
nbasins = np.count_nonzero(minima)

import matplotlib.pyplot as plt 
from matplotlib.cm import tab20b as cmap
cmap.set_bad('white',-1)
        
zones = np.zeros_like(height)
zones[ minima ] = range(1,nbasins+1)
zones[height == 9]  = -1
# print(zones)
# # plt.imshow(zones, cmap='gray')
# # plt.show()
# print('')
k = 0
plt.imshow(zones, cmap=cmap)
plt.title('Iteración: {}'.format(k))
plt.savefig('{}.png'.format(k))
plt.show()
while True:
    for i in range(nrows):
        for j in range(ncols):
            if zones[i,j] > 0:
                try:
                    if zones[i+1,j] == 0:
                        zones[i+1,j] = zones[i,j]
                    elif zones[i+1,j] == -1:
                        pass 
                    else:
                        zones[zones == zones[i+1,j]] = zones[i+1,j]
                except:
                    pass
                try:
                    if i == 0:
                        pass
                    elif zones[i-1,j] == 0:
                        zones[i-1,j] = zones[i,j]
                    elif zones[i-1,j] == -1:
                        pass 
                    else:
                        zones[zones == zones[i-1,j]] = zones[i-1,j]
                except:
                    pass
                try:
                    if zones[i,j+1] == 0:
                        zones[i,j+1] = zones[i,j]
                    elif zones[i,j+1] == -1:
                        pass 
                    else:
                        zones[zones == zones[i,j+1]] = zones[i,j+1]
                except:
                    pass
                try:
                    if j == 0:
                        pass
                    elif zones[i,j-1] == 0:
                        zones[i,j-1] = zones[i,j]
                    elif zones[i,j-1] == -1:
                        pass 
                    else:
                        zones[zones == zones[i,j-1]] = zones[i,j-1]
                except:
                    pass
    k = k+1
    plt.imshow(zones, cmap=cmap)
    plt.title('Iteración: {}'.format(k))
    plt.savefig('{}.png'.format(k))
    plt.show()

    if np.all(zones != 0):
         break
    
    # print(zones)
    # print('')
print(k)

plt.imshow(zones, cmap='tab20b')
plt.show()


labels = set(list(zones[zones>-1].flatten()))
nbasins = len(labels)

size_basins = np.zeros([nbasins], dtype=int)

for i, label in enumerate(labels):
    size_basins[i] = np.count_nonzero( zones == label)

size_basins.sort()

print( np.prod( size_basins[-3:]))

# minvals = height[minima]
# minvals.sort()

# I = np.arange(nrows, dtype=int)
# J = np.arange(ncols, dtype=int)
# I, J = np.meshgrid(I,J)

# label = 1
# for i in range(len(minvals)):
#     if np.any(zones[ np.less_equal(minvals[i],height) & np.less(height,minvals[i+1])])
#     zones[ np.less_equal(minvals[i],height) & np.less(height,minvals[i+1])] = label


# print(height)
# print(zones)



# zones[:,1:] = np.where( zones[:,1:] == 0, zones[:,0:-1], zones[:,1:])
# print(zones)

