from copy import deepcopy

text = open('input17.txt', 'r')

L = text.readlines()

text.close()

d3 = []
matrix = []

for line in L:
    matrix_line = []
    for cube in line:
        if cube != '\n':
            matrix_line.append(cube)
    matrix.append(deepcopy(matrix_line))

d3.append(deepcopy(matrix))

length = len(matrix)
extra = 0

layer1 = []
for i1 in range(length):
    layer_line1 = []
    for j1 in range(length):
        layer_line1.append('.')
    layer1.append(deepcopy(layer_line1))
d3.insert(0, deepcopy(layer1))
d3.append(deepcopy(layer1))


def add_layers(current):
    global length
    layer = []
    layer_line = []
    for i in range(length + 2):
        layer_line.append('.')
    for i in range(length + 2):
        layer.append(deepcopy(layer_line))
    for l in range(length // 2 - extra, length // 2 + extra + 1):
        for i in range(length):
            current[l][i].insert(0, '.')
            current[l][i].append('.')
        current[l].insert(0, deepcopy(layer_line))
        current[l].append(deepcopy(layer_line))
    length += 2
    current.insert(0, deepcopy(layer))
    current.append(deepcopy(layer))
    for i in range(length):
        if not(length // 2 - extra <= i <= length // 2 + extra) and i != 0 and i != len(current):
            current[i] = deepcopy(layer)
    return current, layer_line


def count_active(x, y, z, current):
    global length
    counter = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if x + i < length and y + j < length and z + k < length:
                    if current[x + i][y + j][z + k] == '#' and (i != 0 or j != 0 or k != 0):
                        counter += 1
    return counter


def cycle(pocket):
    global length
    global extra

    pocket, layer_line = add_layers(pocket)

    x = length // 2
    new = deepcopy(pocket)

    for i in pocket:
        for j in i:
            print(j)
        print('\n')

    for i in range(-1, 2):
        for j in range(-2, 3):
            for k in range(-2, 3):
                active = count_active(x + i, x + j, x + k, pocket)
                print(x+i, x+j, x+k, active)
                if pocket[x + i][x + j][x + k] == '#':
                    if active == 2 or active == 3:
                        new[x + i][x + j][x + k] = '#'
                    else:
                        new[x + i][x + j][x + k] = '.'
                else:
                    if active == 3:
                        new[x + i][x + j][x + k] = '#'
                    else:
                        new[x + i][x + j][x + k] = '.'

    for layer in range(len(new)):
        with_active = []
        layer_active = False
        for row in new[layer]:
            if '#' in row:
                layer_active = True
                with_active.append(deepcopy(row))
        if layer_active:
            with_active.insert(0, deepcopy(layer_line))
            with_active.append(deepcopy(layer_line))
            new[layer] = deepcopy(with_active)

    extra += 1

    return new


def final_active_count(pocket):
    counter = 0
    for i in pocket:
        for j in i:
            counter += j.count('#')
    return counter


for time in range(6):
    d3 = deepcopy(cycle(d3))
    for i1 in d3:
        for j1 in i1:
            print(j1)
        print('\n')
    print('\n\n')

print(final_active_count(d3))