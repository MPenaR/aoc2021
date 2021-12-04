import numpy as np
file_name = 'input.txt'
with open(file=file_name) as f:
    data = f.readlines()
data = list( map(  lambda line: line.strip('\n'), data) )

codes = np.zeros( [len(data),len(data[0])],dtype=int)
for i in range(len(data)):
    codes[i] = np.array( list(data[i]) )


#O_rating
Ocode = codes 
i = 0
while len(Ocode) > 1 :
    s = sum(Ocode[:,i])
    if s < len(Ocode) / 2 :
        Ocode = Ocode[Ocode[:,i] == 0, : ]
    else:
        Ocode = Ocode[Ocode[:,i] == 1, : ]
    i = i + 1 

#CO2_rating
CO2code = codes 
i = 0
while len(CO2code) > 1 :
    s = sum(CO2code[:,i])
    if s < len(CO2code) / 2 :
        CO2code = CO2code[CO2code[:,i] == 1, : ]
    else:
        CO2code = CO2code[CO2code[:,i] == 0, : ]
    i = i + 1 

def bin_array_to_decimal( bin ):
    num = 0
    for i, val in enumerate( np.flip(bin) ):
        num = num + val*pow(2,i)
    return num

Orating = bin_array_to_decimal(Ocode[0])
CO2rating = bin_array_to_decimal(CO2code[0])
print( Orating)
print( CO2rating)
print(Orating * CO2rating )

