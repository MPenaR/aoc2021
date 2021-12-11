with open(file='input.txt', mode='r') as f:
    lines = f.readlines()

lines = [ line.strip('\n') for line in lines ]

openers = [ "(", "[", "{", "<"]
closers = [ ")", "]", "}", ">"]
points = { ")" : 3,  "]" : 57, "}" : 1197, ">" : 25137 }
score = 0

opened = []
for line in lines: 
    for symbol in line:
        if symbol in openers:
            opened.append(openers.index(symbol))
        else:
            if closers.index(symbol) == opened[-1]:
                opened.pop()
            else:
                print("Expected {}, but found {} instead.".format(closers[opened[-1]],symbol))
                score += points[symbol]
                break


print(score)