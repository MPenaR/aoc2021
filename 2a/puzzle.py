import numpy as np
file_name = 'input.txt'
with open(file=file_name) as f:
    lines = f.readlines()

commands = []
for line in lines:
    command =  line.split(' ')
    commands.append( [ command[0], int(command[1])])
pos = np.array([0,0])
for command in commands:
    if command[0] == 'forward':
        pos = pos +  command[1]*np.array([1,0])
    if command[0] == 'down':
        pos = pos +  command[1]*np.array([0,1])
    if command[0] == 'up':
        pos = pos +  command[1]*np.array([0,-1])


#print(commands)
print(pos)
print(pos[0]*pos[1])