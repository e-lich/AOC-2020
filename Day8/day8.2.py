text = open('input8.txt', 'r')

orders = text.readlines()

text.close()


def check(orders_new):
    index = 0
    accumulator = 0
    while index < len(orders_new):
        order = orders_new[index]
        if order == 'executed':
            return 0
        else:
            if order[0:3] == 'acc':
                accumulator += int(order[4:])
                orders_new[index] = 'executed'
                index += 1
            elif order[0:3] == 'jmp':
                orders_new[index] = 'executed'
                index += int(order[4:])
            elif order[0:3] == 'nop':
                orders_new[index] = 'executed'
                index += 1
    return accumulator


for i in range(len(orders)):
    order_i = orders[i]
    orders_new = list(orders)
    change = False
    if order_i[0:3] == 'nop':
        orders_new[i] = order_i.replace('nop', 'jmp')
        change = True
    elif order_i[0:3] == 'jmp':
        orders_new[i] = order_i.replace('jmp', 'nop')
        change = True
    if change:
        acc = check(orders_new)
        if acc:
            print('The value in the accumulator is', acc, '\b.')
            break
