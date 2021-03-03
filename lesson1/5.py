income: float = float(input('Please, enter the income: '))
costs: float = float(input('Please, enter the costs: '))

profit: float = income - costs

if profit > 0:
    print('Profit!')

    print(f'Profitability equals: {profit / income}')

    employees_count: int = int(input('Please, enter the employees count: '))
    print(f'Profit per employees: {profit / employees_count}')
else:
    print('Waste!')
