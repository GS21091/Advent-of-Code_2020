# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
 
#### Part 1
data= ''
count = 0

with open("Day_4_input.txt", "r") as file:
    lines = file.read()
    lines = lines.split("\n")

for line in lines:
    data += line + " "
    if line == '':
        continue

data = data.split("  ")
data = data[:-1]

#for i in data:
#    i = i.split()
#    d = {}
#    for items in i:
#        items  = items.split(":")
#        d[items[0]] = items[1]
#        
#    if len(d) == 8:
#        count += 1
#
#    elif len(d) == 7 and "cid" not in d:
#        count += 1
#        
#print(count)

#### Part 2

eye_color = 'amb blu brn gry grn hzl oth'.split()

for i in data:
    i = i.split()
    d = {}
    for items in i:
        items  = items.split(":")
        d[items[0]] = items[1]

    temp = 0

    if (len(d) == 7 or len(d) == 8):
        if "byr" in d and 1920 <= int(d['byr']) <= 2002:
            if "iyr" in d and 2010 <= int(d['iyr']) <= 2020:
                if "eyr" in d and 2020 <= int(d['eyr']) <= 2030:
                    if "ecl" in d and d["ecl"] in eye_color:
                        if "pid" in d and len(d['pid']) == 9:
                            if "hgt" in d and d['hgt'][-1] == 'n':
                                ht = int(d["hgt"][:-2])
                                if 59 <= ht <= 76:
                                    if "hcl" in d and d["hcl"][0] == "#":
                                        for z in d["hcl"][1:]:
                                            if 'a' <= z <= 'f' or 0 <= int(z) <= 9:
                                                temp += 1
                                        if temp == 6:
                                            count += 1

                            elif "hgt" in d and d['hgt'][-1] == 'm':
                                ht = int(d["hgt"][:-2])
                                if 150 <= ht <= 193:
                                    if "hcl" in d and d["hcl"][0] == "#":
                                        for z in d["hcl"][1:]:
                                            if 'a' <= z <= 'f' or 0 <= int(z) <= 9:
                                                temp += 1
                                        if temp == 6:
                                            count += 1

print(count)
