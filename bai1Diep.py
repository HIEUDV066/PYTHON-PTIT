import math
def object(x, y):
		return Point_QueQuan(x, y)
class Point_QueQuan:
	def __init__(self,x , y):
		self.x = x
		self.y = y

	def add_662(self, Point):
		h = self.x + Point.x
		t = self.y + Point.y
		return object(h,t)
	def subtract_662(self, Point):
		h = self.x - Point.x
		t = self.y - Point.y
		return object(h,t)
	def dotProduct_662(self, Point):
		h = self.x * Point.x
		t = self.y * Point.y
		return object(h,t)
	def __str__(self):
		return "({},{})".format(int(self.x), int(self.y))
if __name__ == '__main__':
	a = input().split()
	p1 = Point_QueQuan(int(a[0]), int(a[1]))
	p2 = Point_QueQuan(int(a[2]),int(a[3]))
	print(p1.add_662(p2))
	print(p1.subtract_662(p2))
	print(p1.dotProduct_662(p2))