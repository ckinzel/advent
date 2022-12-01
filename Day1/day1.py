with open("day1in.txt") as f:
    lines = f.readlines()

total = 0
sum = 0

for s in lines:
    if(s != '\n'):
        sum += int(s)
    else:
        if (sum > total):
            total = sum
        sum = 0
        
print(total)