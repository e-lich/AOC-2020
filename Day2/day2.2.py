from operator import xor

text = open('input2.txt', 'r')
lines = text.readlines()

br = 0

for i in range(len(lines)):
    n = lines[i]
    L = n.split()
    M = L[0].split('-')
    index1 = int(M[0]) - 1
    index2 = int(M[1]) - 1
    letter = L[1][0]
    if xor(L[2][index1] == letter, L[2][index2] == letter):
        br += 1

print('There are', br, 'valid passwords.')