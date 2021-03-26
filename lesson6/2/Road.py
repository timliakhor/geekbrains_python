class Road:
    __depth: float = 5.0
    __weight: float = 25.0

    def __init__(self, length: float, width: float):
        self.__length = length
        self.__width = width

    def calculate(self) -> float:
        return self.__width * self.__length * self.__depth * self.__weight


road: Road = Road(5000.0, 20.0)
print(road.calculate())