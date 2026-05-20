import math

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def getX(self): return self.__x
    def getY(self): return self.__y
    
    def setXY(self, x, y):
        self.__x = x
        self.__y = y

    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def display(self):
        # In tọa độ chuẩn (x, y) và không xuống dòng
        print(f"({self.__x}, {self.__y})", end="")

class ColorPoint(Point):
    def __init__(self, x=0, y=0, color="trang"):
        super().__init__(x, y)
        self.__color = color

    def setColor(self, color):
        self.__color = color

    def read(self):
        try:
            # Đọc: x y color
            data = input().split()
            if len(data) >= 3:
                self.setXY(int(data[0]), int(data[1]))
                self.__color = data[2]
        except EOFError:
            pass

    def display(self):
        super().display()
        # In dấu hai chấm và màu sắc (Lưu ý: ": " có khoảng trắng)
        print(f": {self.__color}")

class ColorPointTest:
    def testCase(self):
        try:
            # 1. Khởi tạo cp1(5, 10, "trang") và hiển thị
            cp1 = ColorPoint(5, 10, "trang")
            cp1.display()

            # 2. Khởi tạo cp2 bằng cách đọc từ bàn phím
            cp2 = ColorPoint()
            cp2.read()

            # 3. Dời cp2 đi một độ dời (10, 8)
            cp2.move(10, 8)

            # 4. Hiển thị cp2
            cp2.display()

            # 5. Gán màu mới cho cp2 là "vang" và hiển thị lại
            cp2.setColor("vang")
            cp2.display()
            
        except (EOFError, ValueError, IndexError):
            pass

# Khối chạy chương trình
if __name__ == "__main__":
    tester = ColorPointTest()
    tester.testCase()