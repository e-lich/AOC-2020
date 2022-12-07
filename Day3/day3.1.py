text = open('input3.txt', 'r')

field = text.readlines()

trees = 0

i = 0
j = 0
lines = len(field) - 1
columns = len(field[lines]) - 1

while i <= lines:
    if j > columns:
        j -= columns + 1
    if field[i][j] == '#':
        trees += 1
    i += 1
    j += 3

print('You would encounter', trees, 'trees.')
