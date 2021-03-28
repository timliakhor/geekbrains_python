out_file = open("resources/1_result.txt", "w")
input_str: str = ''

while True:
    input_str = input()
    if input_str == '':
        break
    out_file.write(input_str)

out_file.close()