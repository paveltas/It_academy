# Найти самое длинное слово в веденном предложении.
# Учтите что в предложении есть знаки препинания.

str_ = input('Enter a string: ')


def longest_word(value: str) -> str:
    lst = value.split()
    new_lst = [el.strip(",.\\:;/!?'\"") for el in lst]
    return max(new_lst, key=len)


print('longest word ', longest_word(str_))

# Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def", то должно быть выведено "abcdef".

str_ = input('Enter a string: ')


def only_unique_characters(value: str) -> str:
    return ''.join(dict.fromkeys(value.replace(' ', '')))


print('String with only unique characters ', only_unique_characters(str_))

# Посчитать количество строчных (маленьких) и прописных (больших) букв в веденной строке.
# Учитывать только английские буквы.

str_ = input('Enter a string: ')


def lowercase_and_uppercase_letters(value: str) -> (int, int):
    upper = sum(1 for el in value if 65 <= ord(el) <= 91)
    lower = sum(1 for el in value if 97 <= ord(el) <= 123)
    return 'Number of uppercase letters = {} and lowercase letters = {}'.format(upper, lower)


print(lowercase_and_uppercase_letters(str_))
