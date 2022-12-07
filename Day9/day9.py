text = open('input9.txt', 'r')

L = text.readlines()

text.close()

not_valid = 0

for i in range(26, len(L)):
    valid = False
    for j in range(i - 26, i):
        for k in range(i - 26, i):
            if int(L[j]) + int(L[k]) == int(L[i]):
                valid = True
    if not valid:
        not_valid = int(L[i])
        print('The number', not_valid, 'is not valid.')
        break

for i in range(len(L)):
    index = i
    set_sum = 0
    in_sum = []
    while set_sum < not_valid and index < len(L):
        set_sum += int(L[index])
        in_sum.append(int(L[index]))
        index += 1
    if set_sum == not_valid and len(in_sum) >= 2:
        print('The encryption weakness in this XMAS-encrypted list of numbers is', max(in_sum) + min(in_sum), '\b.')
        break
