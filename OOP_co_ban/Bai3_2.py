import math

class Point:
    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y

    def read(self):
        try:
            data = input().split()
            self.__x = int(data[0])
            self.__y = int(data[1])
        except (IndexError, ValueError):
            pass

    def print(self):
        print(f"({self.__x}, {self.__y})", end="")

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def move(self, dx: int, dy: int):
        self.__x += dx
        self.__y += dy

    def getX(self) -> int:
        return self.__x

    def getY(self) -> int:
        return self.__y

    def setXY(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def distance(self, P=None) -> float:
        if P is None:
            return math.sqrt(self.__x**2 + self.__y**2)
        else:
            return math.sqrt((self.__x - P.getX())**2 + (self.__y - P.getY())**2)

class ColorPoint(Point):
    def __init__(self, x=None, y=None, color=None):
        if isinstance(x, ColorPoint):
            super().__init__(x.getX(), x.getY())
            self.__color = x.getColor()
        elif x is not None and y is not None and color is not None: 
            super().__init__(x, y)
            self.__color = color
        else:  
            super().__init__(0, 1)
            self.__color = "xanh"

    def read(self):

        try:
            data = input().split(maxsplit=2)
            x_val = int(data[0])
            y_val = int(data[1])
            self.setXY(x_val, y_val)
            self.__color = data[2]
        except (IndexError, ValueError):
            pass

    def print(self):
        """Hiển thị thông tin dạng (x, y): color - Có xuống dòng"""
        print(f"({self.getX()}, {self.getY()}): {self.__color}")

    def __str__(self):
        """Định nghĩa chuỗi đại diện phục vụ cho lệnh print(c2) của Grader"""
        return f"({self.getX()}, {self.getY()}): {self.__color}"

    def getColor(self) -> str:
        return self.__color

    def setColor(self, color: str):
        self.__color = color


# =====================================================================
# LỚP COLORPOINTTEST (THEO ĐÚNG KHUNG MẪU HÌNH ẢNH)
# =====================================================================
class ColorPointTest:
    def testCase(self):
        # 1. c1 = ColorPoint() (color mặc định = 'xanh'), in c1
        c1 = ColorPoint()
        print(c1)
        
        # 2. c2 = ColorPoint() rồi c2.read() (đọc 1 dòng x y color), in c2 ban đầu
        c2 = ColorPoint()
        c2.read()
        print(c2)
        
        # 3. c3 = ColorPoint(c2) — sao chép
        c3 = ColorPoint(c2)
        
        # 4. c2.move(5, 5) — dời c2
        c2.move(5, 5)
        
        # 5. In c2 (đã dời) rồi c3 (phải giữ nguyên) theo đúng chuẩn Python: print(obj)
        print(c2)
        print(c3)