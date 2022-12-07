text = open('input11.txt', 'r')

chart = text.readlines()

text.close()

L = []
L_new = []

for i in chart:
    R = []
    for j in i:
        if j != '\n':
            R.append(j)
    L.append(R)

change = True

values = [[-1, -1], [-1, 0], [-1, 1],
          [0, -1], 'none', [0, 1],
          [1, -1], [1, 0], [1, 1]]

while change:
    change = False
    L_new = []
    for row in range(len(L)):
        R = []
        for seat in range(len(L[row])):
            occupied = 0
            for position in values:
                if position != 'none':
                    i = row
                    j = seat
                    if (position[0] != -1 or i != 0) and \
                            (position[0] != 1 or i != len(L) - 1) and \
                            (position[1] != -1 or j != 0) and \
                            (position[1] != 1 or j != len(L[i]) - 1):
                        i += position[0]
                        j += position[1]
                    while L[i][j] != 'L' and L[i][j] != '#' and \
                            (i != row or j != seat) and \
                            (position[0] != -1 or i != 0) and \
                            (position[0] != 1 or i != len(L) - 1) and \
                            (position[1] != -1 or j != 0) and \
                            (position[1] != 1 or j != len(L[i]) - 1):
                        i += position[0]
                        j += position[1]
                    if L[i][j] == '#' and (i != row or j != seat):
                        occupied += 1
            if L[row][seat] == 'L':
                if occupied == 0:
                    R.append('#')
                    change = True
                else:
                    R.append('L')
            elif L[row][seat] == '#':
                if occupied >= 5:
                    R.append('L')
                    change = True
                else:
                    R.append('#')
            else:
                R.append('.')
        L_new.append(R)
    L = list(L_new)

occupied = 0

for i in L:
    for k in i:
        if k == '#':
            occupied += 1

print('There are', occupied, 'occupied seats.')
