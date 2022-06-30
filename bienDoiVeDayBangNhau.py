n = int(input())
line = [int(i) for i in input().split()]
hash = dict()
for i in line:
    sum = 0
    for j in line:
        sum += abs(i-j)
    hash[i] = sum
hash_sorted = sorted(hash.items(),key = lambda x:x[1])
print(hash_sorted[0][1],hash_sorted[0][0])
# tinh tong so buoc tung phan tu 
# phan tu nao co buoc nho nhat thi lay