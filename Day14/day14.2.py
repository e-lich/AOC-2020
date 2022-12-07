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
        address = bin(int(parts[0][4:-1]))[2:]
        address_36 = ''
        for i in range(36 - len(address)):
            address_36 += '0'
        address_36 += address
        result_base = []
        floating = 0
        for i in range(len(address_36)):
            if mask[i] == '0':
                result_base.append(address_36[i])
            else:
                if mask[i] == 'X':
                    floating += 1
                result_base.append(mask[i])
        for options in range(pow(2, floating)):
            result = list(result_base)
            option = bin(options)[2:]
            option_fl = ''
            for i in range(floating - len(option)):
                option_fl += '0'
            option_fl += option
            for number in option_fl:
                for index in range(len(result)):
                    if result[index] == 'X':
                        result[index] = number
                        break
            result_string = ''
            for char in result:
                result_string += char
            mem[int(result_string, 2)] = number_36

result_sum = 0
for key in mem.keys():
    result_sum += int(mem[key], 2)

print('The sum of all values left in the memory is', result_sum, '\b.')