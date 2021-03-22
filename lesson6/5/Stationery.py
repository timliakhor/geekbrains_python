from typing import List

class Stationery:
    def __init__(self, title: str):
        self._title = title

    def draw(self) -> None:
        print('Run Draw')


class Pen(Stationery):
    def __init__(self, title: str):
        super().__init__(title)

    def draw(self) -> None:
        print('Run with pen')


class Pencil(Stationery):
    def __init__(self, title: str):
        super().__init__(title)

    def draw(self) -> None:
        print('Run with pencil')


class Handle(Stationery):
    def __init__(self, title: str):
        super().__init__(title)

    def draw(self) -> None:
        print('Run with handle')


draws: List[Stationery] = [
    Pen('Pen'),
    Pencil('Pencil'),
    Handle('Handle')
]

for value in draws:
    value.draw()
