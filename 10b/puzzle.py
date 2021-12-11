with open(file='input.txt', mode='r') as f:
    lines = f.readlines()

lines = [ line.strip('\n') for line in lines ]
corrupted_lines = []

openers = [ "(", "[", "{", "<"]
closers = [ ")", "]", "}", ">"]
points = { ")" : 3,  "]" : 57, "}" : 1197, ">" : 25137 }
score = 0
print('there are {} lines'.format(len(lines)))

for line in lines: 
    corrupted = False
    opened = []
    for symbol in line:
        if symbol in openers:
            opened.append(openers.index(symbol))
        else:
            if closers.index(symbol) == opened[-1]:
                opened.pop()
            else:
                print("Expected {}, but found {} instead.".format(closers[opened[-1]],symbol))
                score += points[symbol]
                corrupted = True
                break
    corrupted_lines.append(corrupted)

incomplete_lines = [ line for i, line in enumerate(lines) if corrupted_lines[i] == False ]

closing_points = { ")" : 1, "]" : 2, "}" : 3, ">" : 4 }

scores = []
for line in incomplete_lines:
    opened = []
    for symbol in line:
        if symbol in openers:
            opened.append(openers.index(symbol))
        else:
            opened.pop()
    opened.reverse()
    
    closing = ''.join( [ closers[i] for i in opened ] )
    score = 0
    for symbol in closing:
        score = 5*score + closing_points[symbol]
    scores.append(score)

scores.sort()
print(scores[ (len(scores)-1)//2 ])

#print(score)