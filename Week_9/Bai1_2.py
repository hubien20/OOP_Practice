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

class PointTest():
    print("Điểm A")
    a = Point(3, 4)
    print("Tọa độ điểm A: ", end="")
    a.print_point()
    print("\nĐiểm B")
    b = Point()
    b.read()
    print("Tọa độ điểm B: ", end="")
    b.print_point()
    print("\nĐiểm C (đối xứng B qua O)")
    c = Point(-b.getX(), -b.getY())
    print("Tọa độ điểm C: ", end="")
    c.print_point()
    dist_b_o = b.distance()
    print(f"\nKhoảng cách từ B đến gốc O: {dist_b_o:.2f}")
    dist_a_b = a.distance(b)
    print(f"Khoảng cách từ A đến B: {dist_a_b:.2f}")
if __name__ == "__main__":
    PointTest()
