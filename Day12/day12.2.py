text = open('input12.txt', 'r')

instructions = text.readlines()

text.close()

east_west = 0
north_south = 0

sides = ['east', 'south', 'west', 'north']
sides_short = ['E', 'S', 'W', 'N']

value_ew = 'east'
value_ns = 'north'

waypoint_ew = 'east'
waypoint_ns = 'north'

waypoint_value_ew = 10
waypoint_value_ns = 1


def rotate(side, angle, current_direction):
    if side == 'L':
        turns = angle % 360 // 90
        current_index = sides.index(current_direction)
        new_index = current_index - turns
        if new_index < 0:
            new_index += 4
        return sides[new_index]
    elif side == 'R':
        turns = angle % 360 // 90
        current_index = sides.index(current_direction)
        new_index = current_index + turns
        if new_index > 3:
            new_index -= 4
        return sides[new_index]


def move(side, distance, side_ew, side_ns, ew, ns):
    if side in sides:
        side = sides_short[sides.index(side)]
    if (sides[sides_short.index(side)] == side_ew or
            sides[sides_short.index(side)] == side_ns):
        if side == 'E' or side == 'W':
            ew += distance
        else:
            ns += distance
    else:
        if side == 'E' or side == 'W':
            if ew - distance < 0 and side_ew == 'east':
                side_ew = 'west'
            elif ew - distance < 0:
                side_ew = 'east'
            ew = abs(ew - distance)
        else:
            if ns - distance < 0 and side_ns == 'north':
                side_ns = 'south'
            elif ns - distance < 0:
                side_ns = 'north'
            ns = abs(ns - distance)
    return side_ew, side_ns, ew, ns


for instruction in instructions:
    if instruction[0] == 'F':
        value_ew, value_ns, east_west, north_south = move(waypoint_ew, int(instruction[1:]) * waypoint_value_ew,
                                                          value_ew, value_ns, east_west, north_south)
        value_ew, value_ns, east_west, north_south = move(waypoint_ns, int(instruction[1:]) * waypoint_value_ns,
                                                          value_ew, value_ns, east_west, north_south)
    elif instruction[0] in sides_short:
        waypoint_ew, waypoint_ns, waypoint_value_ew, waypoint_value_ns = move(instruction[0], int(instruction[1:]),
                                                                              waypoint_ew, waypoint_ns, waypoint_value_ew, waypoint_value_ns)
    elif instruction[0] == 'L':
        waypoint_ew = rotate('L', int(instruction[1:]), waypoint_ew)
        waypoint_ns = rotate('L', int(instruction[1:]), waypoint_ns)
        if waypoint_ns == 'east' or waypoint_ns == 'west':
            switch = waypoint_ns
            waypoint_ns = waypoint_ew
            waypoint_ew = switch
            switch = waypoint_value_ns
            waypoint_value_ns = waypoint_value_ew
            waypoint_value_ew = switch
    elif instruction[0] == 'R':
        waypoint_ew = rotate('R', int(instruction[1:]), waypoint_ew)
        waypoint_ns = rotate('R', int(instruction[1:]), waypoint_ns)
        if waypoint_ns == 'east' or waypoint_ns == 'west':
            switch = waypoint_ns
            waypoint_ns = waypoint_ew
            waypoint_ew = switch
            switch = waypoint_value_ns
            waypoint_value_ns = waypoint_value_ew
            waypoint_value_ew = switch

print("The Manhattan distance between that location and the ship's starting position is",
      north_south + east_west, '\b.')
