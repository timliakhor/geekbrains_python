from Position import Position

position: Position = Position('Bob', 'Johns', 'Director', {
    'wage': 4000.25,
    'bonus': 2000.0
})

print(position.get_total_income())
print(position.get_full_name())