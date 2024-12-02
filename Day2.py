#Get input
try:
    with open("input.txt", "r") as file:
        data = file.readlines()
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
 
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
    tmp3 = list(set(levels))
    if tmp1 == levels or tmp2 == levels:
        if tmp3 == tmp1 or tmp3 == tmp2:
            flag = True
            for i in range(1, len(levels)):
                test = abs(levels[i] - levels[i-1])
                if test > 3:
                    flag = False
                    break
            if flag == True:
                safe = safe + 1
    
print(safe)
#Loop through levels and check for conditions
