def thuanNghich(n):
    str1 = str(n)
    str2 = str1[::-1]
    if(str1 == str2):
    	return True
    else:
    	return False
def soDep(n):
	count = 0
	while n!=0:
		if (n%10)%2 == 1:
		    return False
		count +=1
		n = n//10
	if(count%2==1):
		return False
	return True
t = int(input())
while t != 0:
	n = int(input())
	i = 10
	while i < n:
		if thuanNghich(i)==True and soDep(i)==True  :
			print(i, end=' ')
		i +=1
	print()
	t -=1