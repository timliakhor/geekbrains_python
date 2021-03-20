source = [3, 4, 5, 3, 4, 6, 7, 7]
target = [i for i in source if source.count(i) < 2]
print(target)
