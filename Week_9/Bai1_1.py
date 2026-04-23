import math

class Point:
    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y

    def read(self):
        x, y = map(int, input("Nhap x y: ").split())
        self.__x = x
        self.__y = y

    def display(self):
        print(f"({self.__x}, {self.__y})")

    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y
    
    def distance(self):
        return math.sqrt(self.__x ** 2 + self.__y ** 2)

    def distanceTo(self, P):
        return math.sqrt((self.__x - P.__x) ** 2 + (self.__y - P.__y) ** 2)
    
if __name__ == "__main__":
    p = Point()
    p.read()
    p.display()

    p1 = Point(3, 4)
    print(p.distance())
    print(p.distance(p1))

    p.move(1, 2)
    p.display()