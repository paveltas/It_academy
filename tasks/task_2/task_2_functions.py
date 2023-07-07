'''
Задание 2.
Функции, методы, тайпинги.
'''


# Реализовать функцию, которая принимает строку и возвращает ее в обратном порядке.
def reverse_string(value):
    return value[::-1]


print(reverse_string('abc'))


# Реализовать фунекцию, которая принимает два параметра: число и степень - и возвращает это число,
# возведенное в степень.
# В случае, если степень не задана пользователем, используется значение 2.0.
def number_raised_to_power(value, power=2.0):
    return value ** power


print(number_raised_to_power(2))


# Реализовать функцию, которая принимает произвольный набор параметров и возвращает кортеж, содержащий
# типы переданных параметров.
def tuple_from_args(*args):
    return tuple(type(el) for el in args)


print(tuple_from_args(1, '2', False, 4.21, {2: 3}))


# Реализовать функцию, которая принимает произвольный набор именованных параметров и возвращает их
# группировку по типу в виде словаря.
# Например, если входные параметры заданы как `a=34, b='some text', c=2, d=1.3, e={1: 2}, f=-3.0`,
# то необходимо вернуть словарь следующего вида:
# {
#   int: [['a', 34], ['c', 2]],
#   str: [['b', 'some text']],
#   float: [['d', 1.3], ['f', -3.0]],
#   dict: [['e', {1: 2}]]
# }
def dct_group_params(**kwargs):
    dct = {}
    for k, v in kwargs.items():
        if type(v) not in dct:
            dct[type(v)] = [[k, v]]
        else:
            dct[type(v)].append([k, v])
    return dct


print(dct_group_params(a=1, b=2.2, c='3', d={'a': 4}, e=5, f='6'))

# Реализовать функцию, которая принимает строку и произвольный набор неименованных и именованных параметров.
# Строка может содержать произвольный набор подстрок вида **, *index* или *name*.
# Вместо ** в строку должен быть подставлен символ *.
# Вместо *index* должен быть подставлен неименованный параметр с индексом index. Должна поддерживаться
# отрицательная индексация.
# Вместо *name* должен быть подставлен именованный параметр с именем name.

str_ = "**Hi**, *-1* and *name1*. **Hello**, *0* and *name2*."
name_args = ['Jacob', 'Oliver', 'Jack']
name_kwargs = {"name1": "Charley", 'name2': 'Thomas'}


def format_string(s, *args, **kwargs):
    for i, arg in enumerate(args):
        s = s.replace(f"*{i}*", str(arg))
        s = s.replace(f"*{-len(args) + i}*", str(arg))
    for name, value in kwargs.items():
        s = s.replace(f"*{name}*", str(value))
    return s.replace("**", "*")


print(format_string(str_, *name_args, **name_kwargs))
