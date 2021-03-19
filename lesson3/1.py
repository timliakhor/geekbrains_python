def divide(x_param: float, y_param: float) -> float:
    if y_param == 0:
        raise Exception("Sorry, division by 0 is not allowed")
    return x_param / y_param


x: float = float(input("Please input first param: "))
y: float = float(input("Please input second param: "))
print(divide(x, y))
