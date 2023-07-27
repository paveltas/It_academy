from collections import Counter

# Списки

# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Входные данные - строка из чисел, разделенная пробелами. Выходные данные - количество пар.
# Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар.


lst = input('Enter numbers ').split()


def pairs_of_elements(value: list) -> int:
    return sum(v * (v - 1) // 2 for v in Counter(value).values())


print('pairs_of_elements ->', pairs_of_elements(lst))


# Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.


def unique_numbers(value: list) -> list:
    dct = {}
    for el in value:
        dct[el] = dct.get(el, 0) + 1
    return [k for k, v in dct.items() if v == 1]


print('unique_numbers ->', unique_numbers([8, 1, 2, 3, 1, 1, 2, 10, 2, 3, 3, 4, 5, 6]))


# Дан список целых чисел. Требуется переместить все ненулевые элементы в левую часть списка,
# не меняя их порядок, а все нули - в правую часть.
# Порядок ненулевых элементов изменять нельзя, дополнительный список использовать нельзя,
# задачу нужно выполнить за один проход по списку. Распечатайте полученный список.


def two_pointers(value: list) -> list:
    left = 0
    right = 0

    while right < len(value):
        if value[right] != 0:
            value[left], value[right] = value[right], value[left]
            left += 1
        right += 1
    return value


print('two_pointers ->', two_pointers([6, 0, 7, 0, 0, 5, 8, 0, 1, 0, 0, 4]))

# Кортежи

# Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.


lst = ['a', 'b', 'c']

tuple_ = tuple(lst)

print("['a', 'b', 'c'] =", tuple_)

# Создайте кортеж ('a', 'b', 'c'), И сделайте из него список.


tuple_ = 'a', 'b', 'c'

lst = list(tuple_)

print("('a', 'b', 'c') =", lst)

# Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.


a, b, c = 'a', 2, 'python'

print("a, b, c = 'a', 2, 'python' ->", 'a = {}, b = {}, c = {}'.format(a, b, c))

# Создайте кортеж из одного элемента,
# чтобы при итерировании по этому элементы последовательно выводились значения 1, 2, 3.
# Убедитесь что len() исходного кортежа возвращает 1.


tuple_ = (1, 2, 3),

for el in tuple_[0]:
    print('tuple_ el ->', el)

print('length tuple_ =', len(tuple_))

# Даны два натуральных числа.
# Вычислите их наибольший общий делитель при помощи алгоритма Евклида (мы не знаем функции и рекурсию).


a = 30
b = 84

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print(a)

# Словари

# Города
# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.
# Учтите, что бывают ситуации когда город с таким называнием бывает в разных странах (Брест есть в Беларуси и Франции)


countries = {
    'Россия': {'Москва', 'Санкт-Петербург', 'Казань', 'Сочи'},
    'США': {'Нью-Йорк', 'Лос-Анджелес', 'Чикаго', 'Майами'},
    'Беларусь': {'Могилев', 'Брест', 'Гомель', 'Минск'},
    'Франция': {'Париж', 'Лион', 'Ницца', 'Брест'},
}
cities = ['Могилев', 'Париж', 'Брест', 'Казань', 'Нью-Йорк', 'Сочи', 'Чикаго']

# Входные данные
# Программа получает на вход количество стран N. Далее идет N строк, каждая строка начинается с названия страны,
# затем идут названия городов этой страны. В следующей строке записано число M,
# далее идут M запросов — названия каких-то M городов, перечисленных выше.


number_of_countries = int(input('Enter first number '))

new_countries_dct = {k: v for i, (k, v) in enumerate(countries.items()) if i < number_of_countries}
print('\n'.join(f'{key} {" ".join(value)}' for key, value in new_countries_dct.items()), end='\n\n')

number_of_cities = int(input('Enter second number '))

new_cities_set = set(cities[:number_of_cities])
print('\n'.join(new_cities_set), end='\n\n')

# Выходные данные
# Для каждого из запроса выведите название страны, в котором находится данный город.


cities_in_new_countries = {value for values in new_countries_dct.values() for value in values}

for city in new_cities_set:
    for country in new_countries_dct:
        if city in new_countries_dct[country]:
            print(f'Город {city} есть в стране {country}.')
    if city not in cities_in_new_countries:
        print(f'Города {city} нет ни в одной стране, в указанных вами рамках.')

# Множества

# Во входной строке записан текст. Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.
# Определите, сколько различных слов содержится в этом тексте.


str_ = '''abc abcd Abc   abcdefg
        abcde abcdef   abcd'''


def set_unique_words(value: str) -> int:
    return len(set(value.lower().split()))


print('set_unique_words ->', set_unique_words(str_))


# Даны два списка чисел.
# Посчитайте, сколько различных чисел содержится одновременно как в первом списке, так и во втором.


def set_intersection(value_1, value_2: list) -> int:
    return len(set(value_1) & set(value_2))


print('set_intersection ->', set_intersection([1, 2, 3, 2], [2, 3, 4, 3, 4]))


# Даны два списка чисел. Посчитайте, сколько различных чисел входит только в один из этих списков.


def set_difference(value_1, value_2: list) -> int:
    return len(set(value_1) - set(value_2))


print('set_difference ->', set_difference([1, 2, 3], [3, 4, 5]))

# Языки
# Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
# Входные данные
# Первая строка входных данных содержит количество школьников N.
# Далее идет N чисел Mi, после каждого из чисел идет Mi строк, содержащих названия языков, которые знает i-й школьник.
# Выходные данные
# В первой строке выведите количество языков, которые знают все школьники.
# Начиная со второй строки - список таких языков.
# Затем - количество языков, которые знает хотя бы один школьник, на следующих строках - список таких языков.


number_of_students = int(input('Enter number of students '))
dct = {}
for n in range(number_of_students):
    number_of_languages = int(input('Enter number of student languages '))
    set_ = set()
    for m in range(number_of_languages):
        set_.add(input('Enter a language '))
    dct[n] = set_

languages_of_everyone = set.intersection(*dct.values())
if languages_of_everyone:
    print(
        f"Количество общих языков студентов равно {len(languages_of_everyone)}.\n{', '.join(languages_of_everyone)}")
else:
    print('Нет языков которые знают все студенты.')

print(f"Все используемые языки: {', '.join(set.union(*dct.values()))}")

# Генераторы списков
# Используйте генератор списков чтобы получить следующий: ['xy', 'xz', 'xv', 'yy', 'yz', 'yv'].


lst_1 = ['x', 'y']
lst_2 = ['y', 'z', 'v']


def generate_combinations(list1, list2):
    return [el1 + el2 for el1 in lst_1 for el2 in lst_2]


print('generate_combinations ->', generate_combinations(lst_1, lst_2))

# Используйте на предыдущий список slice, чтобы получить следующий: ['xy', 'xv', 'yz'].


slice_of_lst = generate_combinations(lst_1, lst_2)[::2]

print('slice_of_lst =', slice_of_lst)

# Используйте генератор списков чтобы получить следующий ['1x', '2x', '3x', '4x'].


lst = [str(el) + 'x' for el in range(1, 5)]

print('el + x =', lst)

# Одной строкой (и одним выражением) удалите элемент '2x' из прошлого списка и напечатайте его.


print('lst.pop(1) =', lst.pop(1))

# Скопируйте список и добавьте в него элемент 2x так, чтобы в исходном списке этого элемента не было.


new_lst = lst.copy() + ['2x']
print('lst, new_lst ->', lst, new_lst)


# Генераторы словарей.
# Создайте словарь с помощью генератора словарей,
# так чтобы его ключами были числа от 1 до 20, а значениями кубы этих чисел.


def cube_numbers(value_1, value_2):
    return {el: el ** 3 for el in range(value_1, value_2 + 1)}


print(f'cube_numbers -> {cube_numbers(1, 20)}')


# Генераторы множеств
# Создайте множество с помощью генератора множеств, состоящее из общих делителей чисел 1000 и 9000.


def find_common_divisors(value_1, value_2):
    return {el for el in range(1, min(value_1, value_2) + 1) if value_1 % el == 0 and value_2 % el == 0}


print(f'find_common_divisors -> {find_common_divisors(1000, 9000)}')

# Создайте генератор, который возвращает строки таблицы умножения от 0 до заданного числа.


number = int(input('Enter the number '))


def tables_generator(value: int):
    return (('\t'.join(str(el1 * el2) for el1 in range(value + 1))) for el2 in range(value + 1))


for table in tables_generator(number):
    print(table)
