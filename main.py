def count_russian_char_in_dictionary(file_path):
    rus_letters = [chr(i) for i in range(ord('А'), ord('я') + 1)]

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    result_dictionary = {}
    for line in lines:
        count_russian_char = sum(1 for char in line if char in rus_letters)
        result_dictionary[count_russian_char] = line.strip()

    return result_dictionary


file_path = 'Lab5_txt.txt'
result = count_russian_char_in_dictionary(file_path)
print(result)
