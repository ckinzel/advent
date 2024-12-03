#Get input
try:
    with open("test.txt", "r") as file:
        data = file.readlines()
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")

def get_inst(memory):
    locations = []
    iter = 0
    while True:
        index = memory.find("mul", iter)
        if index == -1:
            break
        locations.append(index)
        iter = index + 1
    return locations

def parse(instr):
    if instr[3] != '(':
        return -1
    elif instr[7] == ')':
        return 7
    elif instr[8] == ')':
        return 8
    elif instr[9] == ')':
        return 9
    elif instr[10] == ')':
        return 10
    elif instr[11] == ')':
        return 11
    else:
        return -1

total = 0
test = data[0]
indices = get_inst(test)
print(indices)
for index in indices:
    sub = test[index:index+12:1]
    term = parse(sub)
    if term == -1:
        continue
    else:
        process = sub[:term+1]
        process = process.split(",")
        first = process[0]
        first = first[4:]
        second = process[1]
        second = second[:-1]
        total = total + int(first) * int(second)

print(total)