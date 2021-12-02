import numpy as np
file_name = 'input2.txt'
with open(file=file_name) as f:
    l = np.array(f.readlines()).astype('int')
incs = l[1:] - l[:-1]
sum_incs = np.count_nonzero( incs>0)
#print(l)
#print(incs)
print(sum_incs)
