count = 0
arr = []
while count<10:
    line = input()
    line = line.split()
    for i in line:
        count += 1
        arr.append(int(i) % 42)
set2=set()
for i in arr:
    set2.add(i)
print(len(set2))