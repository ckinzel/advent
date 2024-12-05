#Get input
rules = []
pages = []

try:
    with open("test.txt", "r") as file:
        data = file.readlines()
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")

for line in data:
    line = line.strip()
    if len(line) == 5:
        rules.append(line)
    else:
        pages.append(line)

print(rules)