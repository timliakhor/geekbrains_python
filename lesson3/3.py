from typing import List


def return_sum_of_max_elements(*args: float) -> float:
    collection: List[float] = list(args)
    collection.sort(reverse=True)
    return collection[0] + collection[1]


user_input: str = input('Please, input args separated by spaces: ')
numbers: List[float] = list(map(float, user_input.split(' ')))
print(return_sum_of_max_elements(*numbers))
