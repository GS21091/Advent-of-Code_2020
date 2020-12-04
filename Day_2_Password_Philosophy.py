# For example, suppose you have the following list:

### 1-3 a: abcde (there should be atleast 1 to 3 'a' in password) - valid
### 1-3 b: cdefg (there should be atleast 1 to 3 'b' in password) - invalid
### 2-9 c: ccccccccc (there should be atleast 2 to 9 'c' in password) - valid

min = 0
max = 0
alphabet = ''
password = ''
new_count = 0

with open('passwords.txt', 'r') as file:
    lines = file.read()
    lines = lines.split("\n")
    lines = lines[:-2]
    
    for line in lines:
        line = line.split(" ")

        numbers = line[0]
        numbers = numbers.split("-")

        min = int(numbers[0])
        max = int(numbers[1])

        alphabet = line[1][0]

        password = line[2]

#        if min <= password.count(alphabet) <= max:
#            count += 1
#
#print(count)

########## Part - 2
#min = 2; max = 9; alphabet = 'c'; password = 'ccccccccc'
#min = 1; max = 3; alphabet = 'b'; password = 'cdefg'
#min = 1; max = 3; alphabet = 'a'; password = 'abcde'

        count = 0
        for i, n in enumerate(password):
            if n == alphabet and (min == i+1 or max == i+1):
                count += 1

        if count == 1:
            new_count += 1

print(new_count)
