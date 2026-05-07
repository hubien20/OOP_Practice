import math
class Point:
    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y
    def read(self):
        try:
            line = input("Nhập tọa độ (x y): ")
            data = line.split()
            self.__x = int(data[0])
            self.__y = int(data[1])
        except (IndexError, ValueError):
            print("Lỗi: Vui lòng nhập đúng định dạng 2 số nguyên cách nhau bởi khoảng trắng!")  
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
        else:
            dx = self.__x - P.getX()
            dy = self.__y - P.getY()
            return math.sqrt(dx**2 + dy**2)

class PointTest:
    def testCase(self):
        A = Point()
        A.print()
        B = Point()
        B.read()
        B.print()
        B.move(1, 1)
        B.print()
        print(B.distance())
if _name_ == "_main_":
    t = PointTest()
    t.testCase()