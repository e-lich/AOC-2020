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


def count_bags(color):
    if rules[color] == 'no':
        return 0
    else:
        bag_sum = 0
        for bag in rules[color]:
            number_color = bag.split()
            number = number_color[0]
            new_color = number_color[1] + ' ' + number_color[2]
            bag_sum += int(number) + int(number) * count_bags(new_color)
        return bag_sum


print(count_bags('shiny gold'), 'bags are required inside a single shiny gold bag.')