from abc import ABC, abstractmethod
from typing import List


class Clothes(ABC):

    @abstractmethod
    def calculate(self) -> float:
        pass


class Coat(Clothes):

    def __init__(self, v: float):
        self.__v = v

    @property
    def v(self):
        return self.__v

    def calculate(self) -> float:
        return (self.__v / 6.5) + 0.5


class Suit(Clothes):
    def __init__(self, h: float):
        self.__h = h

    @property
    def h(self):
        return self.__h

    def calculate(self) -> float:
        return (self.__h * 2) + 0.3


clothes_list: List[Clothes] = []

coat: Coat = Coat(2.4)
print(coat.v)

suit: Suit = Suit(2.1)
print(suit.h)

clothes_list.append(coat)
clothes_list.append(suit)

sum: float = 0.00
for i in clothes_list:
    res = i.calculate()
    sum += res
    print(res)

print(f"Final result: {sum}")
