#Get input
try:
    with open("test.txt", "r") as file:
        data = file.readlines()
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
def part1(data):
    safe = 0
    #Create reports
    for line in data:
        levels = line.split(' ')
        levels[-1] = levels[-1].strip()
        levels = [int(item) for item in levels]

        tmp1 = levels.copy()
        tmp2 = levels.copy()
        tmp1.sort()
        tmp2.sort(reverse=True)
        if tmp1 == levels or tmp2 == levels:
            flag = True
            for i in range(1, len(levels)):
                test = abs(levels[i] - levels[i-1])
                if test > 3 or test < 1:
                    flag = False
                    break
            if flag == True:
                safe = safe + 1
    print(safe)
def part2(data):
    safe = 0
    count = 0
    #Create reports
    for line in data:
        count = count + 1
        levels = line.split(' ')
        levels[-1] = levels[-1].strip()
        levels = [int(item) for item in levels]
        flag = True
        for i in range(1, len(levels)):
            if levels[-1] > levels[0]:
                test = levels[i] - levels[i-1]
                if test > 3 or test < 1:
                    #tmp = levels.copy()
                    for j in range(len(levels)):
                        flag = True
                        tmp = levels.copy()
                        del tmp[j]#############
                        #tmp.remove(levels[j])
                        for k in range(1, len(tmp)):
                            test2 = tmp[k] - tmp[k-1] ########
                            if test2 > 3 or test2 < 1:
                                flag = False
                                break
                        if flag == True:
                            break
                    if flag == False:
                        break
            elif levels[-1] < levels[0]:
                test = levels[i - 1] - levels[i]
                if test > 3 or test < 1:
                    #tmp = levels.copy()
                    for j in range(len(levels)):
                        flag = True
                        tmp = levels.copy()
                        del tmp[j]
                        #tmp.remove(levels[j])
                        for k in range(1, len(tmp)):
                            test2 = levels[k-1] - levels[k]
                            if test2 > 3 or test2 < 1:
                                flag = False
                                break
                        if flag == True:
                            break
                    if flag == False:
                        break
        if flag == True:
            safe = safe + 1
    print(safe)
part2(data)


