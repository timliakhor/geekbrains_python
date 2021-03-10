from typing import List


def uppercase_first_letter(string: str) -> str:
    return string[0:1].upper() + string[1:]


string_list: List[str] = input('Please, input string: ').split(' ')
result: str = ''

for i, value in enumerate(string_list):
    result += (lambda index: '' if index == 0 else ' ')(i) + uppercase_first_letter(value)

print(result)
