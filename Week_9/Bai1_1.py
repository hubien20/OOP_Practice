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


if __name__ == "__main__":
    p1 = Point()
    print("Điểm p1 mặc định:", end=" ")
    p1.print()

    
    p2 = Point(10, 20)
    print("Điểm p2:", end=" ")
    p2.print()

    
    print("\n--- Nhập dữ liệu cho p1 ---")
    p1.read()
    print("Điểm p1 sau khi nhập:", end=" ")
    p1.print()

    
    p1.move(10, 10)
    print("Điểm p1 sau khi dời (10, 10):", end=" ")
    p1.print()

    
    print(f"\nKhoảng cách từ p1 đến gốc tọa độ: {p1.distance():.2f}")
    print(f"Khoảng cách từ p1 đến p2: {p1.distance(p2):.2f}")