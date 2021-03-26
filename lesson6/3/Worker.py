from typing import Dict


class Worker:
    def __init__(self, name: str, surname: str, position: str, income: Dict[str, float]):
        self._name = name
        self._surname = surname
        self._position = position
        self._income = income
