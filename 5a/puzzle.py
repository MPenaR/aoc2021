import numpy as np
file_name = 'input.txt'
with open(file=file_name,mode='r') as f:
    lines = f.readlines()

pA = []
pB = []
for line in lines: 
    A, B = line.split(' -> ')
    pA.append( A.split(',') )
    pB.append( B.split(',') )

pA = np.array(pA, dtype=int)
pB = np.array(pB, dtype=int)

maxX = max( pA[:,0].max(), pB[:,0].max() )
maxY = max( pA[:,1].max(), pB[:,1].max() )

segments = np.zeros([maxY+1, maxX+1], dtype=int)

for a, b in zip( pA, pB):
    if np.any(a-b == 0) :
        if a[0] == b[0]:
            idx = range(min(a[1],b[1]),max(a[1],b[1])+1)
            segments[ idx, a[0]] = segments[ idx, a[0] ] + 1
        else:
            idx = range(min(a[0],b[0]),max(a[0],b[0])+1) 
            segments[ a[1], idx ] = segments[ a[1], idx ] + 1
#print(segments)
print(np.sum(segments>1))