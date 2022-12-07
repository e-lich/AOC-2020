text = open("input4.txt", "r")

L = text.readlines()

text.close()

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'hcl', 'ecl', 'pid']
allowed_hcl = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
allowed_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

passports = L.count('\n') + 1

valid_passports = 0
index = 0

for i in range(passports):
    not_valid = False
    existing_fields = {}
    while index < len(L) and L[index] != '\n':
        line = L[index].split()
        for j in range(len(line)):
            field = line[j].split(':')[0]
            value = line[j].split(':')[1]
            existing_fields[field] = value
        index += 1
    index += 1
    for k in required_fields:
        if k not in existing_fields.keys():
            not_valid = True
        else:
            if k == 'byr' and (int(existing_fields[k]) < 1920 or int(existing_fields[k]) > 2002):
                not_valid = True
            elif k == 'iyr' and (int(existing_fields[k]) < 2010 or int(existing_fields[k]) > 2020):
                not_valid = True
            elif k == 'eyr' and (int(existing_fields[k]) < 2020 or int(existing_fields[k]) > 2030):
                not_valid = True
            elif k == 'hgt' and existing_fields[k][-2:] != 'cm' and existing_fields[k][-2:] != 'in':
                not_valid = True
            elif k == 'hgt' and existing_fields[k][-2:] == 'cm' and (int(existing_fields[k][0:-2]) < 150 or int(existing_fields[k][0:-2]) > 193):
                not_valid = True
            elif k == 'hgt' and existing_fields[k][-2:] == 'in' and (int(existing_fields[k][0:-2]) < 59 or int(existing_fields[k][0:-2]) > 76):
                not_valid = True
            elif k == 'hcl':
                if existing_fields[k][0] != '#':
                    not_valid = True
                else:
                    for a in range(1, len(existing_fields[k])):
                        if existing_fields[k][a] not in allowed_hcl:
                            not_valid = True
            elif k == 'ecl' and existing_fields[k] not in allowed_ecl:
                not_valid = True
            elif k == 'pid' and len(existing_fields[k]) != 9:
                not_valid = True
    if not not_valid:
        valid_passports += 1

print('There are', valid_passports, 'valid passports.')
