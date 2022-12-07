text = open("input4.txt", "r")

L = text.readlines()
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'hcl', 'ecl', 'pid']

passports = L.count('\n') + 1

valid_passports = 0
index = 0

for i in range(passports):
    not_valid = False
    existing_fields = []
    while index < len(L) and L[index] != '\n':
        line = L[index].split()
        for j in range(len(line)):
            existing_fields.append(line[j].split(':')[0])
        index += 1
    index += 1
    for k in required_fields:
        if k not in existing_fields:
            not_valid = True
    if not not_valid:
        valid_passports += 1

print('There are', valid_passports, 'valid passports.')
