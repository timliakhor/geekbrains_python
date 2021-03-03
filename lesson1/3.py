def add_number(number_arg: int) -> int:
    str_number: str = str(number_arg)
    digit: str = str_number
    if len(str_number) > 1:
        digit = str_number[:1]
    return int(str_number + digit)


input_number: int = int(input('Please, enter the number: '))
result: int = 0
current_number: int = input_number

for i in range(3):
    result = result + current_number
    current_number = add_number(current_number)

print(result)
