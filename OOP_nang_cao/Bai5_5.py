class Temperature:
    def __init__(self, celsius: float = 0.0):
        self._c = 0.0
        self.celsius = celsius 
    @property
    def celsius(self) -> float:
        return self._c
    @celsius.setter
    def celsius(self, value: float):
        if value < -273.15:
            raise ValueError("Nhiệt độ không thể thấp hơn độ không tuyệt đối (-273.15°C)")
        self._c = value

    @property
    def fahrenheit(self) -> float:
        return self._c * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float):

        celsius_value = (value - 32) * 5 / 9

        self.celsius = celsius_value