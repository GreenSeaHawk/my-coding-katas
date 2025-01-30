import pprint
matrix = [
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None]
] 

for i in range(4):
    for j in range(2,-1,-1):
        matrix[j][i] = 'xxx'

pprint.pprint(matrix)           
print('')

matrix = [
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None]
] 

for i in range(4):
    for j in range(5,2,-1):
        matrix[j][i] = 'xxx'

pprint.pprint(matrix)        