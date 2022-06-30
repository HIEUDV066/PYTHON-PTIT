def sang(n):
    danh_dau=[True]*(n+1) 
    
    can=int(n**0.5)+1 
    
    for i in range(2,can+1): 
        if danh_dau[i]==True:    
            for j in range(i*i,n+1,i): 
                danh_dau[j]=False 
    return danh_dau
t = int(input())
a = sang(1000000)
while t!=0:
    n = int(input())
    i = 2
    while i<n:
        j = str(i)[::-1]
        if a[i]==True and a[int(j)]==True and j!=str(i) and i<int(j)<n :
            print(i,j,sep=' ',end=' ')
        i +=1
    print()
    t -= 1