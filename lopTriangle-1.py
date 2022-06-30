from math import sqrt


class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3

    def check(self):
        ab = self.distance(self.x1, self.y1, self.x2, self.y2)
        bc = self.distance(self.x2, self.y2, self.x3, self.y3)
        ca = self.distance(self.x3, self.y3, self.x1, self.y1)
        ok = (ab + bc > ca) and (bc + ca > ab) and (ca + ab > bc)
        if ok:
            self.solve()
        else:
            print("INVALID")

    def distance(self, x1, y1, x2, y2):
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def solve(self):
        r = self.distance(self.x1, self.y1, self.x2, self.y2) + self.distance(self.x2, self.y2, self.x3,
                                                                              self.y3) + self.distance(self.x3, self.y3,
                                                                                                       self.x1, self.y1)
        print("%.3f" % r)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = input().split()
        tg = Triangle(float(arr[0]), float(arr[1]), float(arr[2]), float(arr[3]), float(arr[4]), float(arr[5]))
        tg.check()
