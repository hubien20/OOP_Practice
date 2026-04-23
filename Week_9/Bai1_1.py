import math
class Point:
    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y

    def distance(self, other):
        return math.sqrt((self.__x - other.__x) ** 2 + (self.__y - other.__y) ** 2)

p=Point(x, y)
p.print()
print(p.distance())