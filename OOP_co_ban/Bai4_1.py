import math

class TuLanh:
    def __init__(self, nhanhieu=None, maso=None, nuocsx=None, tkdien=None, dungtich=None, gia=None):
        if isinstance(nhanhieu, TuLanh):
            self.__nhanhieu = nhanhieu.layNhanHieu()
            self.__maso = nhanhieu._TuLanh__maso
            self.__nuocsx = nhanhieu._TuLanh__nuocsx
            self.__tkdien = nhanhieu._TuLanh__tkdien
            self.__dungtich = nhanhieu._TuLanh__dungtich
            self.__gia = nhanhieu.layGia()
            
        elif nhanhieu is not None and maso is not None and nuocsx is not None and tkdien is not None and dungtich is not None and gia is not None:
            self.__nhanhieu = str(nhanhieu)
            self.__maso = str(maso)
            self.__nuocsx = str(nuocsx)
            self.__tkdien = bool(tkdien)
            self.__dungtich = int(dungtich)
            self.__gia = int(gia)
            
        else:
            self.__nhanhieu = "Elextrolux"
            self.__maso = "UNKNOWN"
            self.__nuocsx = "Việt Nam"
            self.__tkdien = True
            self.__dungtich = 256
            self.__gia = 7000000

    def makeCopy(self, tl):
        if isinstance(tl, TuLanh):
            self.__nhanhieu = tl.__nhanhieu
            self.__maso = tl.__maso
            self.__nuocsx = tl.__nuocsx
            self.__tkdien = tl.__tkdien
            self.__dungtich = tl.__dungtich
            self.__gia = tl.__gia

    def nhapThongTin(self):
        try:
            self.__nhanhieu = input().strip()
            self.__maso = input().strip()
            self.__nuocsx = input().strip()
            
            tk_str = input().strip()
            self.__tkdien = True if tk_str.lower() == 'true' else False
            
            self.__dungtich = int(input().strip())
            self.__gia = int(input().strip())
        except (ValueError, IndexError):
            pass

    def __str__(self):
        tk_text = "Có" if self.__tkdien else "Không"
        lines = [
            f"Nhãn hiệu: {self.__nhanhieu}",
            f"Mã số: {self.__maso}",
            f"Nước SX: {self.__nuocsx}",
            f"T/K điện: {tk_text}",
            f"Dung tích: {self.__dungtich}L",    
            f"Giá: {self.__gia}VNĐ"              
        ]
        return "\n".join(lines)

    def print(self):
        print(self.__str__())

    def layNhanHieu(self) -> str:
        return self.__nhanhieu

    def layGia(self) -> int:
        return self.__gia

    def soNguoiSD(self) -> int:
        return self.__dungtich // 100

    def cungNhanHieu(self, tl) -> bool:
        if isinstance(tl, TuLanh):
            return self.__nhanhieu.lower() == tl.layNhanHieu().lower()
        return False

    def nhHon(self, tl) -> bool:
        if isinstance(tl, TuLanh):
            return self.__dungtich < tl._TuLanh__dungtich
        return False