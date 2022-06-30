from decimal import Decimal
import math
class Point:
	def __init__(self,x , y):
		self.x = x
		self.y = y
	def distance(self, Point):
		dx = self.x - Point.x
		dy = self.y - Point.y
		dsquared = math.sqrt(dx**2 + dy**2)
		return "%.4f"%dsquared 
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1