import math

class Point:
    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y

    def read(self):
        try:
            line = input().split()
            if len(line) >= 2:
                self.__x = int(line[0])
                self.__y = int(line[1])
        except EOFError:
            pass

    def print(self):
        print(f"({self.__x}, {self.__y})", end="")

    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def getX(self): return self.__x
    def getY(self): return self.__y
    
    def setXY(self, x, y):
        self.__x = x
        self.__y = y

    def distance(self, p=None):
        if p is None:
            return math.sqrt(self.__x**2 + self.__y**2)
        return math.sqrt((self.__x - p.getX())**2 + (self.__y - p.getY())**2)

class ColorPoint(Point):
    def __init__(self, *args):
        if len(args) == 0:
            super().__init__(0, 1)
            self.__color = "xanh"
        elif len(args) == 3:
            super().__init__(args[0], args[1])
            self.__color = args[2]
        elif len(args) == 1 and isinstance(args[0], ColorPoint):
            super().__init__(args[0].getX(), args[0].getY())
            self.__color = args[0].getColor()

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def read(self):
        try:
            data = input().split()
            if len(data) >= 3:
                self.setXY(int(data[0]), int(data[1]))
                self.__color = data[2]
        except (EOFError, ValueError):
            pass

    def print(self):
        super().print()
        print(f": {self.__color}")