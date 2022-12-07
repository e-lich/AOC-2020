text = open('input5.txt', 'r')

passes = text.readlines()

text.close()

seat_IDs = []

for i in passes:
    min_row = 0
    max_row = 127
    min_column = 0
    max_column = 7
    for r in range(10):
        if i[r] == 'F':
            max_row = (min_row + max_row) // 2
        elif i[r] == 'B':
            min_row = (min_row + max_row) // 2
        elif i[r] == 'L':
            max_column = (min_column + max_column) // 2
        else:
            min_column = (min_column + max_column) // 2
    seat_IDs.append(max_row * 8 + max_column)

for i in range(8, 1017):
    if i not in seat_IDs and (i + 1) in seat_IDs and (i - 1) in seat_IDs:
        print('The ID of your seat is', i, '\b.')

print('The highest seat ID on a boarding pass is', max(seat_IDs), '\b.')