from typing import Tuple, List

SPECIAL_CHARACTER: str = 's'


def sum_chars(strings_param: List[str]) -> Tuple[bool, int]:
    result: int = 0
    for character in strings_param:
        if character == SPECIAL_CHARACTER:
            return False, result
        result += int(character)

    return True, result


is_continue: bool = True
amount: int = 0

while is_continue:
    strings: List[str] = input('Please, input string with numbers, '
                               f' separated by spaces (stop symbol is "{SPECIAL_CHARACTER}") : ').split(' ')
    is_continue, local_amount = sum_chars(strings)
    amount += local_amount
    print(amount)
