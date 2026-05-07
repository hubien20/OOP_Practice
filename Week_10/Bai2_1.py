class Point:
    def  __init__ (self, x=0,y=1):
        self.__x = x
        self.__y = y
    def read(self):
        x, y = map(int, input().split())
        self.__x = x
        self.__y = y
    def print(self):
        print(f"({self.__x}, {self.__y})")
    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def distance(self, P=None):
        if P is None:
            return math.sqrt(self.__x**2 + self.__y**2)
        dx = self.__x - P.getX()
        dy = self.__y - P.getY()
        return math.sqrt(dx**2 + dy**2)
class LineSegment:
    def __init__ (self, p1=None, p2=None):
        if p1 is None and p2 is None:
            self.__d1 = Point(8, 5)
            self.__d2 = Point(1, 0)
        else:
            self.__d1 = p1
            self.__d2 = p2
    def print_line(self):
        print("Đoạn thẳng có hai đầu mút là: ")
        print("Điểm 1: ", end="")
        self.__d1.print()
        print("Điểm 2: ", end="")
        self.__d2.print()
    def length(self):
        return self.__d1.distance(self.__d2)
if __name__ == "__main__":
    A = Point()
    B = Point(3, 4)
    line = LineSegment(A, B)
    line.print_line()
    print("Độ dài đoạn thẳng AB là: ", line.length())