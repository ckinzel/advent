import json

with open("day2in.txt") as f:
    lines = f.readlines()

filtered = [item.strip() for item in lines]
j = open("decode2.json")
decode = json.load(j)

sum = 0

for results in filtered:
    sum += int(decode[results])

print(sum)