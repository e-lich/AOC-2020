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

while change:
    change = False
    L_new = []
    for row in range(len(L)):
        R = []
        for seat in range(len(L[row])):
            s_plus = seat + 1
            s_minus = seat - 1
            r_plus = row + 1
            r_minus = row - 1
            if row == 0:
                r_minus = r_plus
            if seat == 0:
                s_minus = s_plus
            if row == len(L) - 1:
                r_plus = r_minus
            if seat == len(L[row]) - 1:
                s_plus = s_minus
            if L[row][seat] == 'L':
                if (L[row][s_minus] == 'L' or L[row][s_minus] == '.') and \
                        (L[row][s_plus] == 'L' or L[row][s_plus] == '.') and \
                        (L[r_minus][s_minus] == 'L' or L[r_minus][s_minus] == '.') and \
                        (L[r_minus][seat] == 'L' or L[r_minus][seat] == '.') and \
                        (L[r_minus][s_plus] == 'L' or L[r_minus][s_plus] == '.') and \
                        (L[r_plus][s_minus] == 'L' or L[r_plus][s_minus] == '.') and \
                        (L[r_plus][seat] == 'L' or L[r_plus][seat] == '.') and \
                        (L[r_plus][s_plus] == 'L' or L[r_plus][s_plus] == '.'):
                    R.append('#')
                    change = True
                else:
                    R.append('L')
            elif L[row][seat] == '#':
                counter = 0
                if L[row][s_minus] == '#' and seat != 0:
                    counter += 1
                if L[row][s_plus] == '#' and seat != len(L[row]) - 1:
                    counter += 1
                if L[r_plus][s_plus] == '#' and seat != len(L[row]) - 1 and row != len(L) - 1:
                    counter += 1
                if L[r_plus][seat] == '#' and row != len(L) - 1:
                    counter += 1
                if L[r_plus][s_minus] == '#' and row != len(L) - 1 and seat != 0:
                    counter += 1
                if L[r_minus][s_plus] == '#' and row != 0 and seat != len(L[row]) - 1:
                    counter += 1
                if L[r_minus][seat] == '#' and row != 0:
                    counter += 1
                if L[r_minus][s_minus] == '#' and row != 0 and seat != 0:
                    counter += 1
                if counter >= 4:
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
