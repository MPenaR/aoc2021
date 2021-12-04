import numpy as np
file_name = 'input.txt'

def read_table( f, N = 5 ):
    table = np.loadtxt( f, dtype=int, max_rows = N)
    return table
N = 5
with open( file = file_name ) as f : 
    throws = f.readline()
    tables_num = []
    tables_bool = []
    while f.readline():
        tables_num.append( read_table(f) )

Ntables = len(tables_num )
tables_bool = np.zeros( [ Ntables, N, N ], dtype=bool)
tables_num = np.array(tables_num, dtype = int)

throws = np.array( throws.split(','), dtype = int )

for throw in throws:
    tables_bool[ tables_num == throw ] = True
    
    rows = np.all( tables_bool , axis = 2)
    columns =  np.all( tables_bool , axis = 1)
    winners = np.logical_or( np.any(rows, axis=1), np.any(columns, axis=1)) 
    if any(winners):
        print("bingo!!")
        break


print(tables_num[winners,:,:])
print(tables_bool[winners,:,:])
print(throw*np.sum(tables_num[winners,:,:][tables_bool[winners,:,:]==False]))