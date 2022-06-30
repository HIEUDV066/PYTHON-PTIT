def isPrime(num):
    if num > 1:
        for i in range( 2 , int(num / 2) + 1):
            if  (num % i == 0):
                return 0
    return 1
n = int(input())
a = [int(i) for i in input().split()]
dic = dict()
for i in a:
	if i in dic:
		dic[i] +=1
	else:
		if isPrime(i):
			dic[i] = 1
for key in dic:
	print(key,dic[key])