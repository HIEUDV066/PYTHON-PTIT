import math
class Point:
	def __init__(self,x , y):
		self.x = x
		self.y = y
	def distance(self, Point):
		dx = self.x - Point.x
		dy = self.y - Point.y
		dsquared = math.sqrt(dx**2 + dy**2)
		return dsquared 
	def Triangle(self, a, b):
		xy=self.distance(a)
		yz=a.distance(b)
		xz=self.distance(b)
		s = 0.25*math.sqrt((xy+yz+xz)*(xy+yz-xz)*(yz+xz-xy)*(xz+xy-yz))
		if xy+yz>xz and xy+xz>yz and xz+yz>xy:
			return "%.2f"%(s)
		else:
			return "INVALID"
t=int(input())
for i in range(t):
	a=[float(i) for i in input().split()]
	point1=Point(a[0], a[1])
	point2=Point(a[2], a[3])
	point3=Point(a[4], a[5])
	for i in a:
		if abs(i) >= 1000:
			print("INVALID")
	else:
		print(point1.Triangle(point2, point3))
