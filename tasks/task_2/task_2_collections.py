'''
Задание 2.
Коллекции.
Примечание: входные параметры ни в одной из задач не должны быть модифицированы.
'''

import copy
from itertools import zip_longest
from numbers import Number
from typing import Any, Dict, Iterable, List, Tuple


# Сконструировать и вернуть список из переданных аргументов.
def build_list_from_args(*args) -> List:
    return list(args)


print('build_list_from_args ->', build_list_from_args(1, 3, 4, 5, 6, 7))


# Сконструировать и вернуть список из переданных аргументов, имеющих тип int.
def build_int_list_from_args(*args) -> List[int]:
    return [el for el in args if isinstance(el, int)]


print('build_int_list_from_args ->', build_int_list_from_args(1, 'enter', 656, {1, 2, 3}, 5, '23'))


# Сконструировать и вернуть список из переданных аргументов, имеющих заданный тип.
def build_list_from_args_using_type(argument_type: type, *args) -> List:
    return [el for el in args if isinstance(el, argument_type)]


print('build_list_from_args_using_type ->',
      build_list_from_args_using_type(set, 1, 'enter', 656, {1, 2, 3}, 5, '23'))
print('build_list_from_args_using_type ->',
      build_list_from_args_using_type(str, 1, 'enter', 656, {1, 2, 3}, 5, '23'))


# Сконструировать и вернуть список из переданных аргументов, тип которых входит заданное множество.
# Для более эффективной работы преобразовать `argument_types` в `set`.
def build_list_from_args_using_type_set(argument_types: Iterable, *args) -> List:
    set_arg_types = set(argument_types)
    return [el for el in args if type(el) in set_arg_types]


print('build_list_from_args_using_type_set ->',
      build_list_from_args_using_type_set((set, int), 1, 'enter', 656, {1, 2, 3}, 5, '23', True))
print('build_list_from_args_using_type_set ->',
      build_list_from_args_using_type_set((bool, str), 1, 'enter', False, 656, {1, 2, 3}, 5, '23', True))


# Сконструировать и вернуть список из двух списков, переданных в качестве аргументов.
def build_list_from_two_lists(first: List, second: List) -> List:
    return first + second


print('(build_list_from_two_lists ->',
      build_list_from_two_lists([1, 2, 'sdfsfdsd', (2, 3, 1)], ['sfsdfds', 12, True, {1: 'f', 'l': 3}]))


# Сконструировать и вернуть список из неограниченного числа списков, переданных в качестве аргументов.
def build_list_from_list_args(*lists) -> List:
    new_lst = []
    for el in lists:
        new_lst.extend(el)
    return new_lst


print('(build_list_from_list_args ->',
      build_list_from_list_args([1, 2, 'sdfsfdsd', (2, 3, 1)], ['sfsdfds', 12, True, {1: 'f', 'l': 3}],
                                [{1, 43, 65, 'd', 'open'}, False, 43]))


# Сконструировать список из заданного элемента и значения длины (использовать умножение).
def build_list_from_value_and_length(value: Any, length: int) -> List:
    return [value] * length


print('build_list_from_value_and_length ->', build_list_from_value_and_length([1, 'word', {2, 4, 'open'}], 8))


# Удалить из списка заданный элемент.
def remove_value_from_list(values: List, value_to_remove: Any) -> List:
    values.remove(value_to_remove)
    return values


print('remove_value_from_list ->', remove_value_from_list([1, 'word', {2, 4, 'open'}], 'word'))


# Удалить из списка заданный элемент, используя comprehension expression [... for .. in ...].
def remove_value_from_list_using_comprehension(values: List, value_to_remove: Any) -> List:
    return [el for el in values if el != value_to_remove]


print('remove_value_from_list_using_comprehension ->',
      remove_value_from_list_using_comprehension([1, 'word', {2, 4, 'open'}], {2, 4, 'open'}))


# Удалить из списка заданный элемент, используя `filter` и lambda-функцию.
def remove_value_from_list_using_filter(values: List, value_to_remove: Any) -> List:
    return list(filter(lambda x: x != value_to_remove, values))


print('remove_value_from_list_using_filter ->', remove_value_from_list_using_filter([1, 'word', {2, 4, 'open'}], 1))


# Удалить из списка заданные элементы. Преобразовать `values_to_remove` в `set`.
def remove_values_from_list(values: List, values_to_remove: Iterable) -> List:
    values_to_remove = set(values_to_remove)
    return [el for el in values if el not in values_to_remove]


print('remove_values_from_list ->', remove_values_from_list([1, 'word', (2, 4, 'open')], (1, (2, 4, 'open'))))


# Удалить из списка заданные элементы. Преобразовать `values_to_remove` в `set`.
def remove_values_from_list_using_comprehension(values: List, value_to_remove: Any) -> List:
    if not isinstance(value_to_remove, Iterable):
        return remove_value_from_list_using_comprehension(values, value_to_remove)
    return remove_values_from_list(values, value_to_remove)


print('remove_values_from_list_using_comprehension ->',
      remove_values_from_list_using_comprehension([1, 'word', (2, 4, 'open')], 1))


# Удалить из списка заданные элементы. Преобразовать `values_to_remove` в `set`.
# Использовать `filter` и lambda-функцию.
def remove_values_from_list_using_filter(values: List, value_to_remove: Any) -> List:
    if not isinstance(value_to_remove, Iterable):
        return remove_value_from_list_using_filter(values, value_to_remove)
    value_to_remove = set(value_to_remove)
    return list(filter(lambda x: x not in value_to_remove, values))


print('remove_values_from_list_using_filter ->',
      remove_values_from_list_using_filter([1, 'word', (2, 4, 'open')], (1, (2, 4, 'open'))))


# Удалить из списка дублирующиеся значения (использовать преобразование в `set` и обратно).
def remove_duplicates_from_list(values: List) -> List:
    return list(set(values))


print('remove_duplicates_from_list ->', remove_duplicates_from_list([1, 1, 2, 3, 4, 3, 4, 3, 2, 1, 5]))


# Создать и вернуть словарь из заданного набора именованных аргументов, значения которых имеют тип int.
def build_dict_from_named_arguments_of_type_int(**kwargs) -> Dict:
    return {k: v for k, v in kwargs.items() if isinstance(v, int)}


print('build_dict_from_named_arguments_of_type_int ->',
      build_dict_from_named_arguments_of_type_int(a=2, b=3, c=4, d="3", e='word'))


# Создать и вернуть словарь, используя в качестве ключей аргумент функции,
# а в качестве значений - None (dict.fromkeys).
def build_dict_from_keys(values: Iterable) -> Dict:
    return dict.fromkeys(values)


print('build_dict_from_keys ->', build_dict_from_keys([1, 'a', 2, 'b']))


# Условие дублирует предыдущее задание. Сделаю с изменением, что значение по умолчание мы задаем сами.
# Создать и вернуть словарь, используя в качестве ключей аргумент функции,
# а в качестве значений - None (dict.fromkeys).
def build_dict_from_keys(values: Iterable) -> Dict:
    ...


# Создать и вернуть словарь, используя в качестве ключей аргумент функции,
# а в качестве значений - значение по-умолчанию.
def build_dict_from_keys_and_default(values: Iterable, default: Any) -> Dict:
    return dict.fromkeys(values, default)


print('build_dict_from_keys_and_default ->', build_dict_from_keys_and_default([1, 'a', 2, 'b'], 0))


# Создать и вернуть словарь, ключами которого являются индексы элементов,
# а значениями - значения элементов iterable параметров (использовать enumerate и dict comprehension).
def build_dict_from_indexed_values(values: Iterable) -> Dict:
    return {i: v for i, v in enumerate(values)}


print('build_dict_from_indexed_values ->', build_dict_from_indexed_values(['a', 'b', 'c', 'd']))


# Создать и вернуть словарь, собранный на основе списка пар ключ-значение.
def build_dict_from_key_value_pairs(kws: List[Tuple]) -> Dict:
    return dict(kws)


print('build_dict_from_key_value_pairs ->', build_dict_from_key_value_pairs([(1, 'a'), (2, 'b'), (3, 'c')]))


# Создать и вернуть словарь, собранный из двух списков, один из которых
# содержит ключ, а второй - соответствующее значение (использовать zip).
def build_dict_from_two_lists(keys: List, values: List) -> Dict:
    return dict(zip(keys, values))


print('build_dict_from_two_lists ->', build_dict_from_two_lists(['first', 'second'], [1, 2]))


# Сформировать из двух словарей и вернуть его. В случае, если ключи совпадают,
# использовать значение из второго словаря (dict.update).
def build_dict_using_update(first: Dict, second: Dict) -> Dict:
    first.update(second)
    return first


print('build_dict_using_update ->',
      build_dict_using_update({'a': 1, 'b': 2, 'c': 4}, {'b': 'two', 'c': 'four', 'd': 'five'}))


# Обновить словарь (и вернуть его), используя значения именованных аргументов.
# Заменить значение в случае совпадения ключей.
def update_dict_using_kwargs(dictionary: Dict, **kwargs) -> Dict:
    return build_dict_using_update(dictionary, kwargs)


print('update_dict_using_kwargs ->', update_dict_using_kwargs({'a': 1, 'b': 2, 'c': 4}, a='one', c='four', d='five'))


# Обновить словарь (и вернуть его), используя значения именованных аргументов.
# Объединить значения в список в случае совпадения ключей.
def update_and_merge_dict_using_kwargs(dictionary: Dict, **kwargs) -> Dict:
    new_dict = {}
    for k, v in dictionary.items():
        new_dict[k] = [v, kwargs.pop(k)] if k in kwargs else v
    new_dict.update(kwargs)
    return new_dict


print('update_and_merge_dict_using_kwargs ->',
      update_and_merge_dict_using_kwargs({'a': 1, 'b': 2, 'c': 4}, b='two', c='four', d='five'))


# Объединить два словаря и вернуть результат.
# Объединить значения в список в случае совпадения ключей.
def merge_two_dicts(first: Dict, second: Dict) -> Dict:
    return update_and_merge_dict_using_kwargs(first, **second)


print('merge_two_dicts ->', merge_two_dicts({'a': 1, 'b': 2, 'c': 4}, {'b': 'two', 'c': 'four', 'd': 'five'}))


# Объединить два словаря и вернуть результат.
# В случае совпадения ключей:
# - объединить значения рекурсивно, если оба значения - словари;
# - объединить значения в один список, если оба значения - списки;
# - объединить значения в одно множество, если оба значения - множества;
# - объединить значения в список в любом другом случае.
def deep_merge_two_dicts(first: Dict, second: Dict) -> Dict:
    result = dict(copy.deepcopy(first))
    for k, v in second.items():
        if k in result:
            if isinstance(result[k], dict) and isinstance(v, dict):
                result[k] = deep_merge_two_dicts(result[k], v)
            elif isinstance(result[k], list) and isinstance(v, list):
                result[k].extend(v)
            elif isinstance(result[k], set) and isinstance(v, set):
                result[k] |= v
            else:
                result[k] = [result[k], v]
        else:
            result[k] = v
    return result


dict1 = {1: {'a': {1, 2, 3}, 'b': 2, 'c': 3}, 2: '2', 3: '4', 4: {1, 2, 3}, 5: [1, 2, 3], 'a': 10}
dict2 = {1: {'a': 2, 'b': 4, 'd': 5}, 2: '3', 4: {1, 2, 5, 6, 4}, 5: [2, 3, 4], 'a': 20, 'b': 100}
print('deep_merge_two_dicts ->', deep_merge_two_dicts(dict1, dict2))


# Вернуть список, состоящий из ключей, принадлежащих словарю.
def get_keys(dictionary: Dict) -> List:
    return list(dictionary)


print('get_keys ->', get_keys(dict1))


# Вернуть список, состоящий из значений, принадлежащих словарю.
def get_values(dictionary: Dict) -> List:
    return list(dictionary.values())


print('get_values ->', get_values(dict1))


# Вернуть список, состоящий из пар ключ-значение, принадлежащих словарю.
def get_key_value_pairs(dictionary: Dict) -> List[Tuple]:
    return list(dictionary.items())


print('get_key_value_pairs ->', get_key_value_pairs(dict1))


# Реверсировать и вернуть словарь.
def reverse_dict(dictionary: Dict) -> Dict:
    return dict(reversed(dictionary.items()))


print('reverse_dict ->', reverse_dict({1: 'a', 2: 'b'}))


# Удалить из словаря элементы, имеющие пустые значения (None, '', [], {}).
def clear_dummy_elements(dictionary: Dict) -> Dict:
    return {k: v for k, v in dictionary.items() if v not in (None, '', [], {})}


print('clear_dummy_elements ->', clear_dummy_elements({1: None, 2: '', 3: [], 4: {}, 5: '1'}))


# Удалить из словаря дублирующиеся и пустые элементы.
def clear_dummy_and_duplicate_elements(dictionary: Dict) -> Dict:
    new_dct = {}
    for k, v in dictionary.items():
        if v and v not in set(new_dct.values()):
            new_dct[k] = v
    return new_dct


print('clear_dummy_and_duplicate_elements ->',
      clear_dummy_and_duplicate_elements({1: None, 2: '', 3: [], 4: {}, 5: '1', 6: '1', 8: '2'}))


# Обменять в словаре клчи и значения (в качестве значений могут выступать только неизменяемые значения).
def swap_dict_keys_and_values(dictionary: Dict) -> Dict:
    return {v: k for k, v in dictionary.items()}


print('swap_dict_keys_and_values ->', swap_dict_keys_and_values({1: None, 2: '', 5: '1'}))


# Вернуть словарь, отсортированный по ключу. Ключи могут иметь только тип int.
def sort_dict_with_int_keys(dictionary: Dict) -> Dict:
    return dict(sorted(dictionary.items()))


print('sort_dict_with_int_keys ->', sort_dict_with_int_keys({4: 'c', 1: 'a', 3: 'b'}))


# Вернуть словарь, отсортированный по ключу в обратном порядке. Ключи могут иметь только тип int.
def sort_dict_backward_with_int_keys(dictionary: Dict) -> Dict:
    return reverse_dict(sort_dict_with_int_keys(dictionary))


print('sort_dict_backward_with_int_keys ->', sort_dict_backward_with_int_keys({4: 'c', 1: 'a', 3: 'b'}))


# Вернуть словарь, элементы которого сгруппированы по типу ключа.
# В качестве ключей могут выступать: целые числа, дробные числа и строки.
# Приоритет сортировки групп (от высшего к низшему): целые числа, дробные числа, строки.
def group_dict_elements_by_key_type(dictionary: Dict) -> Dict:
    priority = {int: 1, float: 2, str: 3}
    return {k: dictionary[k] for k in sorted(dictionary, key=lambda x: priority.get(type(x), 4))}


print('group_dict_elements_by_key_type ->',
      group_dict_elements_by_key_type({"3": 3, 1: 1, 2.2: 2, "4": 4, 5: 5, 6.6: 6}))


# Вернуть словарь, элементы которого сгруппированы по типу ключа.
# В качестве ключей могут выступать: целые числа, дробные числа и строки.
# Приоритет сортировки групп (от высшего к низшему): целые числа, дробные числа, строки.
# Внутри каждой из групп отсортировать элементы по значениям ключа в обратном порядке.
def group_dict_elements_by_key_type_and_sort(dictionary: Dict) -> Dict:
    priority = {int: 1, float: 2, str: 3}
    return {k: dictionary[k] for k in sorted(dictionary, key=lambda x: (-priority.get(type(x), 4), x), reverse=True)}


print('group_dict_elements_by_key_type_and_sort ->',
      group_dict_elements_by_key_type_and_sort({"3": 3, 1: 1, 2.2: 2, "4": 4, 5: 5, 6.6: 6}))


# Подсчитать количество элементов словаря, имеющих числовой тип, значение которых находится
# в интервале [-10, 25].
def count_dict_elements(dictionary: Dict) -> int:
    return sum(1 for v in dictionary.values() if isinstance(v, Number) and -10 <= v <= 25)


print('count_dict_elements ->', count_dict_elements({"3": -10, '1': 1, '2.2': 2, "4": 4, '5': 25.1, '6.6': 66}))


# Построить и возвратить словарь из двух списков. Количество ключей может превышать
# количество значений. В этом случае (для ключей, оставшихся без соответствующей пары)
# в качестве значений использовать значение None.
def build_dict_from_two_unaligned_lists(keys: List, values: List) -> Dict:
    value_copy = copy.deepcopy(values)
    return {k: v for k, v in zip_longest(keys, value_copy, fillvalue=None)}


print('build_dict_from_two_unaligned_lists ->', build_dict_from_two_unaligned_lists([1, 2, 3, 4], ['a', 'b', 'c']))


# Построить и возвратить словарь из двух списков. Количество ключей может превышать
# количество значений. В этом случае (для ключей, оставшихся без соответствующей пары)
# в качестве значений использовать значение, заданное по-умолчанию.
def build_dict_from_two_unaligned_lists_and_default(keys: List, values: List, default: Any) -> Dict:
    value_copy = copy.deepcopy(values)
    default_copy = copy.deepcopy(default)
    return {k: v for k, v in zip_longest(keys, value_copy, fillvalue=default_copy)}


print('build_dict_from_two_unaligned_lists_and_default ->',
      build_dict_from_two_unaligned_lists_and_default([1, 2, 3, 4], ['a', 'b', 'c'], 'default'))


# Построить и возвратить словарь из двух iterable объектов. Количество ключей может превышать
# количество значений. В этом случае (для ключей, оставшихся без соответствующей пары)
# в качестве значений использовать значение None.
def build_dict_from_two_unaligned_iterables(keys: Iterable, values: Iterable) -> Dict:
    dct = {}
    for key in keys:
        try:
            dct[key] = next(values)
        except StopIteration:
            dct[key] = None
    return dct


print('build_dict_from_two_unaligned_iterables ->',
      build_dict_from_two_unaligned_iterables(iter([1, 2, 3, 4, 5]), iter(['a', 'b', 'c'])))
