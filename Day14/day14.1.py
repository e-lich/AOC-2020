text = open('input14.txt', 'r')

L = text.readlines()

text.close()

mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
mem = {}

for line in L:
    if 'mask' in line:
        mask = line[7:]
    else:
        parts = line.split()
        number = bin(int(parts[2]))[2:]
        number_36 = ''
        for i in range(36 - len(number)):
            number_36 += '0'
        number_36 += number
        result = []
        for i in range(len(number_36)):
            if mask[i] == 'X':
                result.append(number_36[i])
            else:
                result.append(mask[i])
        result_string = ''
        for char in result:
            result_string += char
        mem[parts[0][4:-1]] = result_string

result_sum = 0
for key in mem.keys():
    result_sum += int(mem[key], 2)

print('The sum of all values left in the memory is', result_sum, '\b.')