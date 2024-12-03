#Get input
try:
    with open("input.txt", "r") as file:
        data = file.readlines()
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
def is_safe(record): # silver star

    flag = False
    tmp1 = record.copy()
    tmp2 = record.copy()
    tmp1.sort()
    tmp2.sort(reverse=True)
    if tmp1 == record or tmp2 == record:
        flag = True
        for i in range(1, len(record)):
            test = abs(record[i] - record[i-1])
            if test > 3 or test < 1:
                flag = False
                break
    return flag

def part2(data): # gold star
    safe = 0
    count = 0
    #Create reports
    for line in data:
        count = count + 1
        levels = line.split(' ')
        levels[-1] = levels[-1].strip()
        levels = [int(item) for item in levels]
        flag = True
        if is_safe(levels) == True:
            safe = safe +1
        else:
            for i in range(len(levels)):
                tmp = levels.copy()
                del tmp[i]
                if is_safe(tmp) == True:
                    safe = safe + 1
                    break
    print(safe)
                    
part2(data)


