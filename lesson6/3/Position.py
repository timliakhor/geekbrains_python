from Worker import Worker
from typing import Dict


class Position(Worker):
    def __init__(self, name: str, surname: str, position: str, income: Dict[str, float]):
        super().__init__(name, surname, position, income)

    def get_total_income(self) -> float:
        return self._income['wage'] + self._income['bonus']

    def get_full_name(self) -> str:
        return self._name + ' ' + self._surname
