from typing import List

if __name__ == "__main__":
    input_str: str = input("Enter group of int values, separated by space: ")
    elements: List[str] = input_str.split(' ')
    index: int = 0
    last_index: int = len(elements) // 2
    is_even: bool = True if len(elements) % 2 == 0 else False
    while (index < last_index * 2 and is_even) or (index < (last_index * 2) - 1 and not is_even):
        elements[index], elements[index + 1] = elements[index + 1], elements[index]
        index += 2
    print(elements)
