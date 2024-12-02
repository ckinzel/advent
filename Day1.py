#Get input
try:
    with open("input.txt", "r") as file:
        data = file.readlines()
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
 
#Create lists
list1 = []
list2 = []
for line in data:
    entry = line.split('  ')
    entry[1] = entry[1].strip()
    list1.append(entry[0])
    list2.append(entry[1])
    
#Order lists
list1.sort()
list2.sort()

#Compare and add in a loop
sum = 0
similarity = 0
for i in range(len(list1)):
    sum = sum + abs(int(list1[i]) - int(list2[i]))
    similarity = similarity + int(list2.count(list1[i])) * int(list1[i])

print(similarity)