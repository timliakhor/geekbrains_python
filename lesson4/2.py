source_list = [2, 4, 6, 3, 5, 1, 20, 15, 16, 14]
print(f"source list: {source_list}")
result_list = [num for i, num in enumerate(source_list) if num > source_list[i - 1] and i != 0]

print(result_list)

###############################################################

source_list = [2, 4, 6, 3, 5, 1, 20, 15, 16, 14]
print(f"source list: {source_list}")

result_list = []


def my_fun(source_list):
    for i, num in enumerate(source_list):
        if num > source_list[i - 1] and i != 0:
            yield num


for j in my_fun(source_list):
    result_list.append(j)

print(result_list)
