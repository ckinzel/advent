with open("day1in.txt") as f:
    lines = f.readlines()

total = 0
msum = 0
top = [0, 0, 0]

for s in lines:
    if(s != '\n'):
        msum += int(s)
    else:
        for t in top:
            m = min(top)
            if msum > m:
                index = top.index(m)
                top[index] = msum
                break

        msum = 0
        
print(sum(top))