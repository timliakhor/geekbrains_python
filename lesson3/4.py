from typing import Generator


def my_pow1(x: int, y: int) -> int:
    return x ** y


def my_pow2(x: int, y: int) -> int:
    result: int = x
    for _ in range(1, y):
        result *= x
    return result


def my_pow3(x: int, y: int, n: int = 1) -> int:
    if n == y:
        return x
    return my_pow3(x * input_x, y, n + 1)


def my_pow4(x: int, y: int) -> Generator[int, None, None]:
    yield False, x
    result: int = x
    for j in range(1, y):
        result *= x
        if j == y - 1:
            yield True, result
        else:
            yield False, result


input_x: int = int(input('Please input x: '))
input_y: int = int(input('Please input y: '))
print(my_pow1(input_x, input_y))
print(my_pow2(input_x, input_y))
print(my_pow3(input_x, input_y))

for is_last_item, element in my_pow4(input_x, input_y):
    if is_last_item:
        print(element)
