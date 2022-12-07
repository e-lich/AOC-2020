text = open('input6.txt', 'r')

L = text.readlines()

text.close()

yes_sum = 0

group_yes = []
group_answers = []

for i in L:
    if i == '\n':
        for a in group_answers:
            for y in group_yes:
                if y not in a and y in group_yes_all:
                    group_yes_all.remove(y)
        yes_sum += len(group_yes_all)
        group_yes = []
        group_answers = []
    else:
        for k in i:
            if k not in group_yes and k != '\n':
                group_yes.append(k)
        group_yes_all = list(group_yes)
        group_answers.append(i)

## ovo je za zadnju grupu za koju se to nebi dogodilo inace jer nakon nje nema enter
for a in group_answers:
    for y in group_yes:
        if y not in a and y in group_yes_all:
            group_yes_all.remove(y)

yes_sum += len(group_yes_all)

print('The sum of those counts is', yes_sum, '\b.')
