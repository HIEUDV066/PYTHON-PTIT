t = int(input())

def tich(num):
    res = 1
    for i in str(num):
        res *= int(i)
    return res

while t:
    t -= 1

    n = int(input())
    arr = []
    nhap = input()
    nhap = nhap.split()

    for i in nhap:
        arr.append(int(i))
    arr.sort()
    hash = dict()
    for i in arr:
        hash[int(i)] = tich(i)
    # print(hash)
    hash_sorted = sorted(hash.items(), key = lambda x:x[1],reverse=False)
    for i in hash_sorted:
        print(i[0]," ",end="")
    print("")