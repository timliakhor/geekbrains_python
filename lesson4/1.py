from sys import argv

script_name, work_hours, salary_per_hour, benefit = argv


def calculate_salary(work_hours: int, salary_per_hour: float, benefit: float) -> float:
    return work_hours * salary_per_hour + benefit


print(calculate_salary(int(work_hours), float(salary_per_hour), float(benefit)))
