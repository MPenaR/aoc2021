with open( file = 'input.txt', mode='r') as f:
    lines = [ line.split(' | ') for line in f.readlines()]

bases = [ [ frozenset(code) for code in line[0].split(' ') ] for line in lines ]
codes = [ [ frozenset(code) for code in line[1].strip('\n').split(' ') ] for line in lines ]
original_codes = [ frozenset(code) for code in [ 'abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg' ] ]


def get_mapping(base):
    
    n_segments = [ len( word ) for word in base ]

    mapping = {}

    one = base[ n_segments.index(2) ]
    seven = base[ n_segments.index(3)]
    four = base[ n_segments.index(4)]
    eight = base[ n_segments.index(7)]

    a = seven.difference(one)
    mapping[a] = 'a'


    nine = [ number for number in filter(lambda n: len(n) == 6, base) if set(a | four).issubset(number)][0]

    g = nine.difference(a | four)
    mapping[g] = 'g'

    e = eight.difference(nine)
    mapping[e] = 'e'

    six = [ number for number in filter(lambda n: len(n) == 6, base) if not one.issubset( number )][0]
    f = six & one
    mapping[f] = 'f'

    c = one.difference(f)
    mapping[c] = 'c'

    zero = [ number for number in filter(lambda n: len(n) == 6, base) if ( set(one) | e ).issubset( number )][0]

    d = eight.difference(zero)
    mapping[d] = 'd'

    three = [ number for number in filter(lambda n: len(n) == 5, base) if ( one ).issubset( number )][0] 

    b = nine.difference(three)
    mapping[b] = 'b'

    return mapping

def converter( code, mapping):
    n_code = ''.join( [ mapping[frozenset(letter)] for letter in code ] )
    i = original_codes.index(frozenset(n_code))
    return i

sum = 0
for base, code in zip(bases,codes):
    mapping = get_mapping(base)
    num = int( ''.join( [ str( converter( c, mapping) ) for c in code ] ) )
    sum += num

print(sum)