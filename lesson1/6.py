def increase_result(prev_result: float) -> float:
    return prev_result + prev_result / 10


day: int = 1

a: float = float(input('Please, enter a: '))
b: float = float(input('Please, enter b: '))

while a < b:
    day = day + 1
    a = increase_result(a)

print(f'Result {day}')
