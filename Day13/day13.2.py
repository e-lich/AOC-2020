text = open('input13.txt', 'r')

L = text.readlines()

text.close()

departed = False

buses = L[1].split(',')
integer_buses = []
N = 1

for i in buses:
    if i != 'x':
        integer_buses.append(int(i))
        N *= int(i)

x = 0

for i in range(len(buses)):
    if buses[i] != 'x':
        Ni = N // int(buses[i])
        if i % int(buses[i]) != 0:
            bi = int(buses[i]) - i
        else:
            bi = 0
        product = bi * Ni
        xi = 1
        found = False
        while not found:
            if (Ni * xi) % int(buses[i]) == 1:
                found = True
            else:
                xi += 1
        product *= xi
        x += product

# while not departed:
#     departed = True
#     for i in range(len(buses)):
#         if buses[i] != 'x':
#             if (time + i) % int(buses[i]) != 0:
#                 departed = False
#                 break
#     time += max(integer_buses)
#     print(time)

print('The result is', x % N, '\b.')
