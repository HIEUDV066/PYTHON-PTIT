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
    count = 0
    while i+6<n:
        if (a[i]==True and a[i+2]==True and a[i+6]==True) :
            count += 1
        else:
            if (a[i]==True and a[i+4]==True and a[i+6]==True):
                count +=1
        i += 1
    print(count)
    t -= 1