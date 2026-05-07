import math

class Point:
    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y

    def print(self):
        print(f"({self.__x}, {self.__y})")

    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def getX(self): return self.__x
    def getY(self): return self.__y

    def distance(self, p=None):
        if p is None:
            return math.sqrt(self.__x**2 + self.__y**2)
        return math.sqrt((self.__x - p.getX())**2 + (self.__y - p.getY())**2)

class LineSegment:
    def __init__(self, *args):
        if len(args) == 0:
            self.__d1 = Point(8, 5)
            self.__d2 = Point(1, 0)
        elif len(args) == 1 and isinstance(args[0], LineSegment):
            s = args[0]
            self.__d1 = Point(s.getD1().getX(), s.getD1().getY())
            self.__d2 = Point(s.getD2().getX(), s.getD2().getY())
        elif len(args) == 2:
            self.__d1 = args[0]
            self.__d2 = args[1]
        elif len(args) == 4:
            self.__d1 = Point(args[0], args[1])
            self.__d2 = Point(args[2], args[3])

    def print(self):
        print(f"[({self.__d1.getX()}, {self.__d1.getY()}); ({self.__d2.getX()}, {self.__d2.getY()})]")

    def move(self, dx, dy):
        self.__d1.move(dx, dy)
        self.__d2.move(dx, dy)

    def length(self):
        return self.__d1.distance(self.__d2)

    def angle(self):
        dx = self.__d2.getX() - self.__d1.getX()
        dy = self.__d2.getY() - self.__d1.getY()
        deg = math.degrees(math.atan2(dy, dx))
        if deg < 0: deg += 360
        return int(round(deg))

    def getD1(self): return self.__d1
    def getD2(self): return self.__d2

class LineSegmentTest:
    def testCase(self):
        try:
            data = input().split()
            if len(data) < 4: return
            x1, y1, x2, y2 = map(int, data)
            
            ls1 = LineSegment(x1, y1, x2, y2)
            ls1.print()
            print(float(ls1.length())) 
            print(ls1.angle())
            ls2 = LineSegment(ls1)
            ls1.move(1, 1)
            ls1.print()
            ls2.print()
            
        except EOFError:
            pass