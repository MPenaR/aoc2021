with open( file = 'input.txt', mode='r' ) as f:
    population = [ int(age) for age in f.readline().split(',') ]

#print( "Initial state: {}".format(population))

Ndays = 256

for i in range(1,Ndays+1):
    newborns = 0
    for j in range(len(population)):
        if population[j] == 0:
            population[j] = 6
            newborns = newborns + 1
        else:
            population[j] = population[j] - 1
    
    population = population + newborns*[8]
    #print( "After  {} day/s: {}".format(i,population))
print(len(population))

