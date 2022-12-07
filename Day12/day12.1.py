text = open('input12.txt', 'r')

instructions = text.readlines()

text.close()

east_west = 0
north_south = 0

currently_facing = 'east'

sides = ['east', 'south', 'west', 'north']
sides_short = ['E', 'S', 'W', 'N']

value_ew = 'east'
value_ns = 'north'

for instruction in instructions:
    if instruction[0] == 'F':
        if currently_facing == 'east' or currently_facing == 'west':
            if currently_facing == value_ew or east_west == 0:
                east_west += int(instruction[1:])
            else:
                if east_west - int(instruction[1:]) < 0 and value_ew == 'east':
                    value_ew = 'west'
                elif east_west - int(instruction[1:]) < 0:
                    value_ew = 'east'
                east_west = abs(east_west - int(instruction[1:]))
        else:
            if currently_facing == value_ns or north_south == 0:
                north_south += int(instruction[1:])
            else:
                if north_south - int(instruction[1:]) < 0 and value_ns == 'north':
                    value_ns = 'south'
                elif north_south - int(instruction[1:]) < 0:
                    value_ns = 'north'
                north_south = abs(north_south - int(instruction[1:]))
    elif instruction[0] in sides_short:
        if (sides[sides_short.index(instruction[0])] == value_ew or
           sides[sides_short.index(instruction[0])] == value_ns):
            if instruction[0] == 'E' or instruction[0] == 'W':
                east_west += int(instruction[1:])
            else:
                north_south += int(instruction[1:])
        else:
            if instruction[0] == 'E' or instruction[0] == 'W':
                if east_west - int(instruction[1:]) < 0 and value_ew == 'east':
                    value_ew = 'west'
                elif east_west - int(instruction[1:]) < 0:
                    value_ew = 'east'
                east_west = abs(east_west - int(instruction[1:]))
            else:
                if north_south - int(instruction[1:]) < 0 and value_ns == 'north':
                    value_ns = 'south'
                elif north_south - int(instruction[1:]) < 0:
                    value_ns = 'north'
                north_south = abs(north_south - int(instruction[1:]))
    elif instruction[0] == 'L':
        turns = int(instruction[1:]) % 360 // 90
        current_index = sides.index(currently_facing)
        new_index = current_index - turns
        if new_index < 0:
            new_index += 4
        currently_facing = sides[new_index]
    elif instruction[0] == 'R':
        turns = int(instruction[1:]) % 360 // 90
        current_index = sides.index(currently_facing)
        new_index = current_index + turns
        if new_index > 3:
            new_index -= 4
        currently_facing = sides[new_index]

print("The Manhattan distance between that location and the ship's starting position is",
      north_south + east_west, '\b.')