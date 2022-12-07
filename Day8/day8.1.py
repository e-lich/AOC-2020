text = open('input8.txt', 'r')

orders = text.readlines()

text.close()

index = 0
acc = 0

while orders[index] != 'executed':
    order = orders[index]
    if order[0:3] == 'acc':
        acc += int(order[4:])
        orders[index] = 'executed'
        index += 1
    elif order[0:3] == 'jmp':
        orders[index] = 'executed'
        index += int(order[4:])
    elif order[0:3] == 'nop':
        orders[index] = 'executed'
        index += 1

print('The value in the accumulator is', acc, '\b.')
