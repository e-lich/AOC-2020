text = open('input7.txt', 'r')

L = text.readlines()

text.close()

rules = {}

for i in L:
    line_words = i.split()

    key = line_words[0] + ' ' + line_words[1]

    index = 4

    if line_words[4] == 'no':
        rules[key] = 'no'
    else:
        rules[key] = []
        while ',' in line_words[index + 3]:
            value = line_words[index] + ' ' + line_words[index + 1] + ' ' + line_words[index + 2]
            rules[key].append(value)
            index += 4
        value = line_words[index] + ' ' + line_words[index + 1] + ' ' + line_words[index + 2]
        rules[key].append(value)

check_for = ['shiny gold']
check_for_next = []
done = False
outside_bag_possibilities = []

while not done:
    done = True
    for k in check_for:
        for i in rules.keys():
            for j in rules[i]:
                if k in j:
                    done = False
                    check_for_next.append(i)
                    if i not in outside_bag_possibilities:
                        outside_bag_possibilities.append(i)
    check_for = list(check_for_next)
    check_for_next = []

print(len(outside_bag_possibilities), 'bag colors can eventually contain at least one shiny gold bag.')
