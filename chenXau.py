s1 = input()
s2= input()
n = int(input())
s1 = s1[:n-1] + s2 + s1[n-1:]
print(s1)