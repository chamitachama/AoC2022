
with open("input1", "r") as f:
    lines = f.readlines()

groups = []
group = []

for line in lines:
    line = line.strip()

    if len(line) == 0:
        groups.append(group)
        group = []
    else: 
        group.append(int(line))
groups.append(group)

sums = []

mas_grande = 0
for group in groups:
    acc = 0
    for num in group:
        acc = num + acc
    sums.append(acc)

sums.sort()

Acc = 0
for num in sums[-3:]:
    Acc = num + Acc 
print (Acc)


mas_grande = 0
for sum in sums:
    if sum > mas_grande:
        mas_grande = sum


    

