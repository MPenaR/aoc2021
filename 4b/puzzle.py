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
last_winners = np.zeros([Ntables], bool)
for throw in throws:
    tables_bool[ tables_num == throw ] = True
    
    rows = np.all( tables_bool , axis = 2)
    columns =  np.all( tables_bool , axis = 1)
    winners = np.logical_or( np.any(rows, axis=1), np.any(columns, axis=1))
    new_winners = np.logical_and( winners, np.logical_not(last_winners))
    if all(winners):
        print('bigo...')
        break
    last_winners = winners

print(throw)
print(tables_num[new_winners,:,:])
print(tables_bool[new_winners,:,:])
print(throw*np.sum(tables_num[new_winners,:,:][tables_bool[new_winners,:,:]==False]))