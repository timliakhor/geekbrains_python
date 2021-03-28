from typing import List, Dict
import json

firms: Dict[str, float] = {}
info: List[Dict[str, float]] = []


def avg_profitability_calculator(line: str) -> (int, float, str, float):
    split_line = line.split(' ')
    income: float = float(split_line[2])
    costs: float = float(split_line[3])
    return 1 if income > costs else 0, income - costs if income > costs else 0, split_line[0], costs - income


with open("resources/7.txt", 'r') as file:
    sum: float = 0
    count: int = 0
    for line in file:
        result = avg_profitability_calculator(line)
        count += result[0]
        sum += result[1]
        firms[result[2]] = result[1] if result[0] != 0 else result[3]

    avg_dict = {
        'average_profit': sum / count
    }

    info.append(firms)
    info.append(avg_dict)

    print(info)

    with open("resources/7_result.txt", "w") as write_f:
        json.dump(info, write_f)
