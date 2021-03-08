input_number: str = input('Please, enter the number: ')

index: int = 0
max_value: int = 0

while index < len(input_number):
    if int(input_number[index]) > max_value:
        max_value = int(input_number[index])
    index = index + 1

print(f"Max value: {max_value}")
