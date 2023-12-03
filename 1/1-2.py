def open_file_and_populate_list():
    values = []
    file = open("data.txt", "r")
    lines = file.readlines()
    for line in lines:
        for i in range(len(line)):
            line = line.replace('\n', '')
        values.append(line)
    return values

def convert_word_to_num(lines: list):
    words_and_nums = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 
                      'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    new_list = []
    for line in lines:
        print(line)
        for i in words_and_nums:
            if i in line:
                num = words_and_nums.get(i)
                line = line.replace(i, i[0] + num + i[-1])
                print(line)
        new_list.append(line)   
    return new_list

def remove_anything_else(lines: list):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    cleaned = []
    for line in lines:
        for i in line:
            if i not in numbers:
                line = line.replace(i, '')
        cleaned.append(line)
    return cleaned

def concat_and_add(values):
    final_nums = []
    answer = 0
    for value in values:
        if len(value) > 1:
            num = value[0] + value[-1]
            final_nums.append(num)
        else:
            num = value + value
            final_nums.append(num)

    for number in final_nums:
        answer = answer + int(number)
    return answer

def main():
    lines = open_file_and_populate_list()
    converted = convert_word_to_num(lines)
    numbers_only = remove_anything_else(converted)
    answer = concat_and_add(numbers_only)
    print(answer)

main()