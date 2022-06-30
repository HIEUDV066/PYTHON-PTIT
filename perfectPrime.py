import math
def snt(n):
    if n<2:
        return False
    i=2
    while i <= math.sqrt(n):
        if(n%i == 0):
            return False
        i+=1
    return True
t = int(input())
while t!=0:
	n = input()
	tong=0
	k = True
	for i in n:
		if not(i=='2' or i=='3' or i=='5' or i=='7')==True:
			k= False
		tong +=int(i)
	n1 = n[::-1]
	if snt(int(i))==True and snt(int(n1))==True and snt(tong)==True and k==True:
		print("Yes")
	else:
		print("No")
	t -= 1