# Day 7 of Advent of code
# how many colors can, contain at least one shiny gold bag?
import re

#### part 1

data = {}
count = 0
text = "shiny gold"
text_del = "bags contain"

with open("Day_7_example_1.txt", "r") as file:
    lines = file.read().split("\n")[:-2]

#for line in lines:
#    search = re.findall(r"[a-z]+\s[a-z]+", line)
#
#    new_search = search.copy()
#
#    if text_del in new_search:
#        search.remove(text_del)
#
#    data[search[0]] = search[1:]
#
#s = []
#
#for key, value in data.items():
#    if text in value:
#        s.append(key)
#
#
#for item in s:
#    for keys in data:
#        if item in data[keys]:
#            s.append(keys)
#
#print(len(set(s)))

##### Part 2

for line in lines:
    search_1 = re.findall(r"[a-z]+\s[a-z]+", line)
    search_2 = re.findall(r"\d\s[a-z]+\s[a-z]+",line)

    data[search_1[0]] = search_2
w = []

for key, values in data.items():
    for value in values: 
        if text == key:
            w.append(value)

final = {}
total = 0
x = []

for item in w:
    for key in data:
        if data[key] == []:
            break
        if key in item:
            w.append(data[key][0])
            if item[0] in final:
                x.append(data[key][0])
            else:
                x = data[key]
                final[item[0]] = x
    
print(final)

for key, value in final.items():
    value_total = 0
    for item in value:
        for i in range(1, len(value)):
            value_total += int(item[0]) ** i

    total += value_total + int(key)
print(total)
#for key, value in final.items():
#    value_total = 0
#    for item in value:
#        value_total += int(item[0])
#    total += int(key) * (1 + value_total)
#
#print(total)
