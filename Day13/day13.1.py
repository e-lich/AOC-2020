text = open('input13.txt', 'r')

L = text.readlines()

text.close()

earliest = int(L[0])
time = earliest
departed = False

buses = L[1].split(',')

while not departed:
    for i in range(len(buses)):
        if buses[i] != 'x':
            if time % int(buses[i]) == 0:
                print('The result is', (time - earliest) * int(buses[i]), '\b.')
                departed = True
    time += 1
