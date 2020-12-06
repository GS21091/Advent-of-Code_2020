# day 6 of Advent of code

input_example = "abc abc abac aaaa b".split()

total = 0
#for i in input_example:
#    count = len(set(i))
#    print(count)
#    total += count
#
#print(total)

#### Part 1

total = 0
data = ''

with open("Day_6_input.txt", "r") as file:
    lines = file.read().split("\n")[:-2]
    
for line in lines:

    data += line + ' '

    if line == ' ':
        continue
    

data = data.split("  ")
#print(data)

#for d in data:
#    d = set(d)
#    if " " in d:
#        d.remove(" ")
#    count = len(d)
#    total += count
#
#print(total)

#### Part 2

for s in data:
    s = s.split(" ")
    if "" in s:
        s.remove("")

    res = set("qwertyuiopasdfghjklzxcvbnm")

    for x in s:
        x = set(x)
        res &= x

    count = len(res)
    
    total += count

print(total)
