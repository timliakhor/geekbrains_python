from typing import List

numbers: List[int] = [7, 5, 3, 3, 2]

if __name__ == "__main__":
    user_input: int = int(input("Please, enter a number: "))

    if user_input in numbers:
        last_index: int = len(numbers) - 1 - numbers[::-1].index(user_input)
        numbers.insert(last_index + 1, user_input)
    else:
        if user_input < numbers[0]:
            numbers.append(user_input)
        else:
            numbers.insert(0, user_input)

    print(numbers)
