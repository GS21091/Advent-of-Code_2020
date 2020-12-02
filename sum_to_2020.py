# Sum of 2 entries should be 2020 and return the multiplication of those
# numbers



new_list= []
with open('entries.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
#    for line in lines:
#        new_list.append(line)
#
#content = []
#for i in new_list:
#    new = i.split("\n")
#    content.append(new[0])
#
#content = content[:-1]
#for i in range(len(content)):
#    for j in range(i+1, len(content)):
#        for k in range(j+1, len(content)):
#            if int(content[i]) + int(content[j]) + int(content[k]) == 2020:
#                m = int(content[i]) * int(content[j]) * int(content[k])
#                print(m)
#                print(content[i], content[j], content[k])
#
