
text = open('input2.txt', 'r')
lines = text.readlines()

br = 0

for i in range(len(lines)):
    n = lines[i]
    L = n.split()
    M = L[0].split('-')
    min = int(M[0])
    max = int(M[1])
    letter = L[1][0]
    if min <= L[2].count(letter) <= max:
        br += 1

print('There are', br, 'valid passwords.')