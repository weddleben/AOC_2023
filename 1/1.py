import string

def open_file_and_populate_list():
    file = open(f"data.txt", "r")
    lines = file.readlines()
    return lines

def sanitize_data(lines):
    initial_nums = []
    letters = string.ascii_lowercase
    for line in lines:
        for i in range(len(line)):
            for letter in letters:
                line = line.replace(letter, '')
                line = line.replace('\n', '')
        initial_nums.append(line)
    return initial_nums

def add_numbers(values):
    final_nums = []
    answer = 0
    for value in values:
        if len(value) > 1:
            num = str(value[0]) + str(value[-1])
            final_nums.append(num)
        else:
            num = str(value) + str(value)
            final_nums.append(num)

    for number in final_nums:
        answer = answer + int(number)
    return answer

def main():
    lines = open_file_and_populate_list()
    list_of_nums = sanitize_data(lines)
    answer = add_numbers(list_of_nums)
    print(answer)

main()