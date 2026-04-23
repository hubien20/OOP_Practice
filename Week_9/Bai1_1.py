import math
class Point:
    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y
    def read(self):
        self.__x = int(input("Nhap x: "))
        self.__y = int(input("Nhap y: "))
    def display(self):
        print(f"({self.__x}, {self.__y})")
    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def distance(self, other):
        return math.sqrt((self.__x - other.__x) ** 2 + (self.__y - other.__y) ** 2)
    
x, y = map(int, input().split())
p = Point(x, y)
p.display()
print(p.distance())