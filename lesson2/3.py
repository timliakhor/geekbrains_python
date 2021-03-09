from typing import List, Dict

seasons_month: Dict[str, List[int]] = {
    'Winter': [12, 1, 2],
    'Spring': list(range(3, 6)),
    'Summer': list(range(6, 9)),
    'Autumn': list(range(9, 12)),
}

month_seasons: Dict[int, str] = {}

for key, value in seasons_month.items():
    for element in value:
        month_seasons[element] = key

if __name__ == "__main__":
    user_input: int = int(input("Please, enter number of month: "))
    print(month_seasons[user_input])
