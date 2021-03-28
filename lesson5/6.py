from typing import Set, Dict

lesson_types: Set[str] = {
    '(л)', '(пр)', '(лаб)'
}


def sum_all_lessons(line: str) -> int:
    sum: int = 0
    for part_of_line in line.split(' '):
        for value in lesson_types:
            index = part_of_line.find(value)
            if index != -1:
                sum += int(part_of_line[:index])

    return sum


with open("resources/6.txt", 'r') as file:
    result: Dict[str, int] = {}
    for line in file:
        result[line[:line.find(':')]] = sum_all_lessons(line)

print(result)
