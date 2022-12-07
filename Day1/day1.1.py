
L = []
n = 1

while n != '0':
    n = input()
    L.append(int(n))

for i in range(len(L)):
    for j in range(len(L)):
        if L[i] + L[j] == 2020:
            print(L[i] * L[j])
            break

