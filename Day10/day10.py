text = open('input10.txt', 'r')

L = text.readlines()

text.close()

integer_list = []

for i in L:
    integer_list.append(int(i))

diff1 = 0
diff2 = 0
diff3 = 0

rating = 0

while rating != max(integer_list):
    if (rating + 1) in integer_list:
        rating += 1
        diff1 += 1
    elif (rating + 2) in integer_list:
        rating += 2
        diff2 += 1
    elif (rating + 3) in integer_list:
        rating += 3
        diff3 += 1


def check_max(r, r_list):
    sum_pos = 0
    if r == max(r_list):
        return 1
    else:
        possibilities = []
        if (r + 1) in r_list:
            possibilities.append(r + 1)
        if (r + 2) in r_list:
            possibilities.append(r + 2)
        if (r + 3) in r_list:
            possibilities.append(r + 3)
        for p in possibilities:
            sum_pos += check_max(p, r_list)
        return sum_pos


diff3 += 1
rating += 3

print('There are', diff1, 'differences of 1 jolt and', diff3, 'differences of 3 jolts.')
print('The result is:', diff1, '*', diff3, '=', diff1 * diff3, '\b.')
print('The total number of distinct ways you can arrange the adapters\nto connect the charging outlet to your '
      'device is', check_max(0, integer_list), '\b.')
