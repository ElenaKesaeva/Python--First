"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return list(map(lambda number: number ** 2, numbers))


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(numbers_list):
    primes = []
    for i in numbers_list:
        c = 0
        for j in range(1, i):
            if i % j == 0:
                c += 1
        if c == 1:
            primes.append(i)


def filter_numbers(numbers_list, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)


    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == ODD:
        return list(filter(lambda number: number % 2 != 0, numbers_list))

    if filter_type == EVEN:
        return list(filter(lambda number: number % 2 == 0, numbers_list))

    if filter_type == PRIME:
        return is_prime(numbers_list)



