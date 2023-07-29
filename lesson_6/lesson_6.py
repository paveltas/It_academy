# Выведите n-ое число Фибоначчи, используя только временные переменные,
# циклические операторы и условные операторы. n - вводится.

n = int(input('Введите номер числа Фибоначчи '))


def fibonacci_number(value: int):
    first = 0
    second = 1

    if value == 1:
        return print(f"Под номером 1 число Фибоначчи равно {first}")

    elif value == 2:
        return print(f"Под номером 2 число Фибоначчи равно {second}")

    for _ in range(2, value):
        temp = second
        second = first + second
        first = temp
    return print(f"Под номером {value} число Фибоначчи равно {second}")


fibonacci_number(n)

# Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
# Число положительное целое, произвольной длины.
# Задача требует работать только с числами (без конвертации числа в строку или что-нибудь еще).


number = int(input("Введите число: "))


def palindrome(value: int):
    n = value
    reversed_number = 0

    while n > 0:
        reversed_number = (reversed_number * 10) + (n % 10)
        n //= 10
    return print('Введенное число палиндром') if value == reversed_number else print('Введенное число не палиндром')


palindrome(number)

# Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
# кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz.


for el in range(1, 101):
    if el % 3 == 0 and el % 5 == 0:
        print('FizzBuzz')
    elif el % 3 == 0:
        print('Fizz')
    elif el % 5 == 0:
        print('Buzz')
    else:
        print(el)
