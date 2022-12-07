text = open('input16.txt', 'r')

read = text.readlines()

text.close()

rules = []
nearby_tickets = []

i = 0

while read[i] != '\n':
    rules.append(read[i].replace('\n', ''))
    i += 1

i += 2
your_ticket = read[i].replace('\n', '').split(',')
i += 3

for value in read[i:]:
    nearby_tickets.append(value.replace('\n', '').split(','))

intervals = []
rules_intervals = []
rule_names = []

for i in rules:
    rule_names.append(i.split(' ')[0])
    rule_interval = [i.split(' ')[1].split('-'), i.split(' ')[3].split('-')]
    rules_intervals.append(rule_interval)
    intervals.append(i.split(' ')[1].split('-'))
    intervals.append(i.split(' ')[3].split('-'))

valid_nearby_tickets = list(nearby_tickets)

for ticket in nearby_tickets:
    for value in ticket:
        error = True
        for allowed in intervals:
            if int(allowed[0]) <= int(value) <= int(allowed[1]):
                error = False
                break
        if error:
            valid_nearby_tickets.remove(ticket)

possible = []
possible_strings = []
for i in range(len(your_ticket)):
    possible.append(list(rule_names))
    possible_strings.append('')

for ticket in valid_nearby_tickets:
    for value in ticket:
        for rule in rules_intervals:
            error = True
            for interval in rule:
                if int(interval[0]) <= int(value) <= int(interval[1]):
                    error = False
                    break
            if error:
                if rule_names[rules_intervals.index(rule)] in possible[ticket.index(value)]:
                    possible[ticket.index(value)].remove(rule_names[rules_intervals.index(rule)])

while '' in possible_strings:
    for rule in possible:
        if len(rule) == 1:
            possible_strings[possible.index(rule)] = rule[0]
            for left in possible:
                if rule[0] in left and left != rule:
                    left.remove(rule[0])

solution = 1

for field in possible_strings:
    if 'departure' in field:
        solution *= int(your_ticket[possible_strings.index(field)])

print('If you multiply those six values together you get', solution, '\b.')
