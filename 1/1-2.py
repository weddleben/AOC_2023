numbers_as_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
words_and_nums = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

def open_file_and_populate_list():
    file = open(f"data.txt", "r")
    lines = file.readlines()
    return lines

def sanitize_data(lines):
    initial_nums = []
    for line in lines:
        for i in range(len(line)):
            line = line.replace('\n', '')
        initial_nums.append(line)
    return initial_nums