with open( file = 'input.txt', mode='r' ) as f:
    population = [ int(age) for age in  f.readline().split(',') ]

Ndays = 256

fish_per_age = 9*[0]
for fish in population:
    fish_per_age[ fish ] +=  1 

for i in range(Ndays):
    births = fish_per_age[0]
    fish_per_age[:8] = fish_per_age[1:]
    fish_per_age[8] = births
    fish_per_age[6] = fish_per_age[6] + births  

print(sum(fish_per_age))