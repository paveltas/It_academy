# coding=utf-8
'''
Задание 1.
Базовые математические операции, приоритеты выполнения, условные операторы, циклы.
'''

from typing import Tuple


# Реализовать функции сложения, вычитания и умножения двух чисел.
def add_mul(first: float, second: float) -> Tuple[float, float, float]:
    return first + second, first - second, first * second


print("add_mul ->", add_mul(4.7, 3.5))


# Реализовать функции деления, деления нацело и нахождения остатка от деления.
def div_int_rem(first: float, second: float) -> Tuple[float, float, float]:
    return first / second, first // second, first % second


print("div_int_rem ->", div_int_rem(6.8, 3.5))


# Обменять два целочисленных значение с помощью битового xor не используя промежуточноые переменные.
def xor_swap(first: int, second: int) -> Tuple[int, int]:
    first ^= second
    second ^= first
    first ^= second
    return first, second


print("xor_swap ->", xor_swap(32, 45))


# Вернуть наименьшее число, используя условный оператор.
def min_conditional(first: float, second: float) -> float:
    return first if first < second else second


print("min_conditional ->", min_conditional(21.5, 21.9))


# Реализовать функции умножения на 2, 8 и 32 с помощью битовых операций сдвига.
def mul_shift_2_8_32(value: int) -> Tuple[int, int, int]:
    return value << 1, value << 3, value << 5


print("mul_shift_2_8_32 ->", mul_shift_2_8_32(2))


# Реализовать функции деления на 2, 8 и 32 с помощью битовых операций сдвига.
def div_shift_2_8_32(value: int) -> Tuple[int, int, int]:
    return value >> 1, value >> 3, value >> 5


print("div_shift_2_8_32 ->", div_shift_2_8_32(128))


# Реализовать операцию возведения в степень остатка от деления.
def exponentiation(divident: float, divider: float, power: float) -> float:
    return (divident % divider) ** power


print("exponentiation ->", exponentiation(14.4, 5.3, 3.3))


# Определить знак 32-битного числа с помощью операции &.
def sign(value: int) -> str:
    return "+" if 1 & (value >> 31) == 0 else "-"


print("sign ->", sign(147483648))


# Умножить целочисленное значение на -1 с помощью битовых операций и сложения.
def change_sign(value: int) -> int:
    return ~value + 1


print("change_sign ->", change_sign(1223))


# Возвратить True, если хотя бы один четный бит 32-х битного числа установлен в 1.
def check_32_even_bit_set(value: int) -> bool:
    return 0xAAAAAAAA & value != 0


print("check_32_even_bit_set ->", check_32_even_bit_set(0x55555555))
print("check_32_even_bit_set ->", check_32_even_bit_set(0xAAAAAAAA))


# Посчитать количество бит в 32-х битном числе, установленных в ноль.
def calculate_32_zero_bits(value: int) -> int:
    return format(value, "b").count("0")


print("calculate_32_zero_bits ->", calculate_32_zero_bits(345678))


# Упаковать два целочисленных значения в 8 бит.
# Первое число должно располагаться в 4 младших битах, второе число в - 4 старших.
def pack_4_4(first: int, second: int) -> int:
    return first | (second << 4)


print("pack_4_4 ->", pack_4_4(13, 12))


# Распоковать два целочисленных значения из 8 бит.
# Первое число должно располагаться в 4 младших битах, второе число в - 4 старших.
def unpack_4_4(value: int) -> Tuple[int, int]:
    return value & 0b00001111, value >> 4


print("unpack_4_4 ->", unpack_4_4(205))


# Ограничить число заданным интервалом. Нижняя граница заданного интервала меньше либо равна верхней.
def clamp(value: float, low: float, high: float) -> float:
    return max(min(high, value), low)


print("clamp ->", clamp(15.4, 1.6, 15.3))


# Ограничить число заданным интервалом. Нижняя граница может быть как меньше, так и больше верхней.
def clamp_any(value: float, low: float, high: float) -> float:
    return max(min(high, value), low) if high > low else max(min(low, value), high)


print("clamp_any ->", clamp_any(5.4, 15.6, 6.8))


# Вернуть True, если число нечетно и входит в интервал от -10 до 10.
def event_and_match_interval_m10_10(value: int) -> bool:
    return -10 < value < 10 and value % 2 != 0


print("event_and_match_interval_m10_10 ->", event_and_match_interval_m10_10(-5))
print("event_and_match_interval_m10_10 ->", event_and_match_interval_m10_10(2))
print("event_and_match_interval_m10_10 ->", event_and_match_interval_m10_10(-11))


# Определить порядок выолнения операций и расстваить скобки таким образом, чтобы он стал обратным.
def reverse_operations(value: float):
    return value ** (4 * (0.5 + 0.25))


print("reverse_operations ->", reverse_operations(6.4))


# Установить n-ый бит числа в единицу.
def set_nth_bit(value: int, n: int) -> int:
    return value | (1 << n)


print("set_nth_bit ->", set_nth_bit(4, 0))


# Переключить n-ый бит числа.
def switch_nth_bit(value: int, n: int) -> int:
    return value ^ (1 << n)


print("switch_nth_bit ->", switch_nth_bit(5, 1))


# Расставить скобки таким образом, чтобы выражение в задаче было возведено в степень 3.
def change_priorities(x: float) -> float:
    return (x + 3) ** 3


print("change_priorities ->", change_priorities(7.1))

'''
Задачи повышенной сложности.
'''


# Ковертировать целое число в формат float32.
# Для того, чтобы разобраться с форматом, можно использовать следующие источники:
# https://goo.su/ipKzbY
# https://learn.microsoft.com/ru-ru/cpp/build/ieee-floating-point-representation?view=msvc-170
# https://habr.com/ru/post/337260/
# Для решения этой задачи нужно также выяснить, как конвертировать байты в целые и дробные числа.
def int_to_float(value: int) -> float:
    return ...


# Вернуть наименьшее целое число без использования условных операторов и встроенных функций.
def min_raw(first: int, last: int) -> int:
    return (first > last) * last + (last > first) * first


print("min_raw ->", min_raw(-2, 4))
