from functools import reduce

with open("resources/5_res_1.txt", 'a') as file:
    for j in [i for i in range(1, 20) if i % 2 == 0]:
        file.write(str(j) + ' ')

with open("resources/5_res_1.txt", 'r') as file:
    print(reduce(lambda previous_element, current_element: previous_element + current_element,
                 list(map(int, file.readline().strip().split(' ')))))
