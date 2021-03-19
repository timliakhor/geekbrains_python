from functools import reduce

even_numbers = [x for x in range(100, 1001) if x % 2 == 0]
print(reduce(lambda previous_element, current_element: previous_element * current_element, even_numbers))
