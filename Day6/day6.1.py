text = open('input6.txt', 'r')

L = text.readlines()

text.close()

yes_sum = 0

group_yes = []

for i in L:
    if i == '\n':
        yes_sum += len(group_yes)
        group_yes = []
    else:
        for k in i:
            if k not in group_yes and k != '\n':
                group_yes.append(k)

yes_sum += len(group_yes)

print('The sum of those counts is', yes_sum, '\b.')
