from time import time

text = open('input16.txt', 'r')

read = text.readlines()

text.close()

rules = []
nearby_tickets = []

i = 0

while read[i] != '\n':
    rules.append(read[i].replace('\n', ''))
    i += 1

i += 2
your_ticket = read[i].replace('\n', '').split(',')
i += 3

for value in read[i:]:
    nearby_tickets.append(value.replace('\n', '').split(','))

intervals = []

for i in rules:
    intervals.append(i.split(' ')[1].split('-'))
    intervals.append(i.split(' ')[3].split('-'))


def overlapping(l1, l2):
    if int(l1[1]) < int(l2[0]) or int(l2[1]) < int(l1[0]) or l1 == l2:
        return False
    else:
        return True


def merge_intervals(l1, l2):
    if int(l1[0]) <= int(l2[0]) <= int(l1[1]) and int(l1[0]) <= int(l2[1]) <= int(l1[1]):
        new = l1
    elif int(l2[0]) <= int(l1[0]) <= int(l2[1]) and int(l2[0]) <= int(l1[1]) <= int(l2[1]):
        new = l2
    elif int(l1[0]) <= int(l2[0]) <= int(l1[1]):
        new = [l1[0], l2[1]]
    else:
        new = [l2[0], l1[1]]
    return new


def merge_intervals_in_list(l):
    finish = []
    for list1 in l:
        overlapped = False
        for list2 in l:
            if overlapping(list1, list2):
                merged = merge_intervals(list1, list2)
                if merged not in finish:
                    finish.append(merged)
                    l.remove(list2)
                overlapped = True
        if not overlapped and list1 not in finish:
            finish.append(list1)
    return finish


def keep_merging(interval_list):
    l_new = merge_intervals_in_list(interval_list)
    while interval_list != l_new:
        interval_list = list(l_new)
        l_new = merge_intervals_in_list(interval_list)
    for left in interval_list:
        left[0] = int(left[0])
        left[1] = int(left[1])
    return interval_list


start = time()
final = keep_merging(intervals)
error_rate = 0

for ticket in nearby_tickets:
    for value in ticket:
        error = True
        for allowed in final:
            if allowed[0] <= int(value) <= allowed[1]:
                error = False
                break
        if error:
            error_rate += int(value)

print('The ticket scanning error rate is', error_rate, '\b.')
end = time()
print('Finished in', end - start, 'seconds.')
