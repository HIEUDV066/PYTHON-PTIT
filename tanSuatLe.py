t = int(input())
while t!=0:
    t-=1
    line  = input()
    arr = [int(i) for i in input().split()]
    dic = dict()
    dem = 0
    for i in arr:
        dic[i]=0
    for i in arr:
        dic[i] +=1
    for i in dic:
        if dic[i]%2==1:
            print(i)