text = open('input3.txt', 'r')

field = text.readlines()

result = 1

lines = len(field) - 1
columns = len(field[lines]) - 1

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

for r in range(len(slopes)):
    i = 0
    j = 0
    trees = 0
    while i <= lines:
        if j > columns:
            j -= columns + 1
        if field[i][j] == '#':
            trees += 1
        i += slopes[r][1]
        j += slopes[r][0]
    result *= trees
    r += 1

print('If you multiply together the number of trees encountered on each of the listed slopes,'
      '\nyou get', result, '\b.')
