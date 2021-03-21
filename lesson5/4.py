from typing import Dict

numbers: Dict[str, str] = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}


def write_in_new_file(line: str, line_number: int) -> None:
    with open(f"resources/4_res_{line_number}.txt", 'w') as f_obj:
        arr = line.split(' ')
        f_obj.write(numbers[arr[0]] + ' ' + arr[1] + ' ' + arr[2])


with open("resources/4.txt") as file:
    for i, line in enumerate(file):
        write_in_new_file(line, i)
