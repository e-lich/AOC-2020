text = open('input15.txt', 'r')

spoken_numbers = text.readline().split(',')

text.close()

number_turns = {}

turn = 1

for i in spoken_numbers:
    number_turns[i] = [turn, 1]
    turn += 1

last = spoken_numbers[-1]

while turn < 2021:
    if number_turns[last][1] == 1:
        last = '0'
    else:
        new_last = str(turn - 1 - number_turns[last][0])
        number_turns[last][0] = turn - 1
        last = new_last
        if last not in number_turns.keys():
            number_turns[last] = [turn, 0]
    number_turns[last][1] += 1
    turn += 1

print('The 2020th number spoken is', last, '\b.')
