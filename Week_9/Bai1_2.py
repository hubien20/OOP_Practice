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
    def distance(self):
        return math.sqrt((self.__x) ** 2 + (self.__y) ** 2)
class PointTest:
A = Point(3, 4)
print("Điểm A:"); A.hien_thi()
xb = int(input("Nhập x của B: "))
yb = int(input("Nhập y của B: "))
B = Point(xb, yb)
print("Điểm B:"); B.hien_thi()
C = B.doi_xung_qua_O()
print("Điểm C (đối xứng B qua O):"); C.hien_thi()
print(f"Khoảng cách B đến O: {B.khoang_cach_den_O():.2f}")
print(f"Khoảng cách A đến B: {A.khoang_cach_den(B):.2f}")
x, y = map(int, input().split())
p = Point(x, y)
p.display()
print(p.distance())