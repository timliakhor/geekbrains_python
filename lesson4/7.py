from math import factorial


def factorial_with_recursion(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return factorial(n - 1) * n


def gen(max_value: int):
    for i in range(1, max_value + 1):
        yield factorial_with_recursion(i)


for i in gen(int(input('Please, enter max value:')) + 1):
    print(i)


