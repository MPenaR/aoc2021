import numpy as np
file_name = 'test.txt'
with open(file=file_name) as f:
    lines = f.readlines()

commands = []
for line in lines:
    dir, val =  line.split(' ')
    commands.append( [ dir, int(val)])

pos = np.array([0,0])
aim = 0
for command in commands:
    if command[0] == 'forward':
        pos = pos +  command[1]*np.array([1, aim])
    if command[0] == 'down':
        aim = aim +  command[1]
    if command[0] == 'up':
        aim = aim -  command[1]

#print(commands)
print(pos)
print(pos[0]*pos[1])