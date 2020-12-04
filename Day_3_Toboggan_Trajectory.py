# find number of trees in the path of 3 right and 1 down

j = 0
pattern = ''
count = 0

x = int(input("Enter x (right movement): "))
y = int(input("Enter y (down movement): "))

with open("Day_3_input.txt", 'r') as path:
    lines = path.read()
    lines = lines.split("\n")

for line in lines[y::y]:

    line = line * 1000

    if len(line) == 0:
        break

    if line[x + j] == "#":
        count += 1
    j += x

print(count)

#### Part - 2 
# check for below and return multiplication of all slopes
#    Right 1, down 1. slope = 2 (example) 
#    Right 3, down 1. slope = 7 (example)
#    Right 5, down 1. slope = 3 (example)
#    Right 7, down 1. slope = 4 (example)
#    Right 1, down 2. slope = 2 (example)

# 43 * 77 *  218 * 65 * 82 = 3847183340
