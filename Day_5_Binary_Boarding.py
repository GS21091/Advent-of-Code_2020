# Day : 5 - Binary Boarding

### Part 1

total_rows = [i for i in range(1, 127)]
total_cols = [j for j in range(0, 8)]
row = 0
column = 0
seat_ids = []

####Examples
#lines = "FBFBBFFRLR BFFFBBFRRR FFFBBBFRRR BBFFBBFRLL".split()

with open("Day_5_input.txt", "r") as file:
    lines = file.read().split("\n")
    lines = lines[:-2]

for line in lines:
    # calculate row 
    rlow = 1
    rhigh = 126
    tr = total_rows[:]
    tc = total_cols[:]
    clow = 0
    chigh = 7


    for i in line[:7]:
        avg = (rlow + rhigh) // 2 
        if i == "F":
            tr = tr[rlow : avg + 1]
            rhigh = avg - 1

        elif i == "B":
            tr = tr[avg: rhigh + 1]
            rlow = avg + 1
            avg += 1
        
    row = avg
        
    # calc column
    for j in line[7:]:
        avg = (clow + chigh) // 2 
        if j == "L":
            tc = tr[clow : avg + 1]
            chigh = avg - 1

        elif j == "R":
            tc = tr[avg : chigh + 1]
            clow = avg + 1
            avg += 1

    column = avg
#    print(row, column)
    seat_id = row * 8 + column
    seat_ids.append(seat_id)

seat_ids = sorted(seat_ids)
print(max(seat_ids))

### Part 2
for i in range(min(seat_ids), max(seat_ids) + 1):
    if i not in seat_ids:
        out = i
print(out)
