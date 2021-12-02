import numpy as np
file_name = 'input.txt'
with open(file=file_name) as f:
    depths = np.array(f.readlines()).astype('int')
window = depths[:-2] + depths[1:-1] + depths[2:] 
incs = window[1:] - window[:-1]
sum_incs = np.count_nonzero( incs>0)
#print(window)
#print(incs)
print(sum_incs)
