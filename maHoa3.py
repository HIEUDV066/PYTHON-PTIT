s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def Devid(str):
	str1=str[0:len(str)//2]
	str2=str[len(str)//2:]
	return str1,str2
def Rotate(str):
	k=0
	s1=''
	for i in str:
		k += s.find(i)
	for i in str:
		s1 += s[(s.find(i)+k)%26]
	return s1
def DRM(str):
	str1,str2 = Devid(str)
	s1 = Rotate(str1)
	s2 = Rotate(str2)
	s3 = ''
	for i in range(len(s1)):
		s3 +=s[(s.find(s1[i])+s.find(s2[i]))%26]
	return s3
n = int(input())
while n!=0:
	n -=1
	str = input()
	print(DRM(str))