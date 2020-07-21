# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.

import random

a = list(input('Введите диапазон от и до через ПРОБЕЛ\n>').split())
b = input('Выберите нужно число\n1. Вещественное\n2. Целое\n>')

try:
    if b == '1':
        print(round(random.random() * (float(a[1]) - float(a[0])) + float(a[0]), 2))
    elif b == '2':
        print(random.randint(int(a[0]), int(a[1])))
except:
    print('Неверно введенные значения')


def random_letter(start, stop):
    """Yield a range of lowercase letters."""
    for ord_ in range(ord(start.lower()), ord(stop.lower())):
        yield chr(ord_)


rl = list(random_letter('b', 'f'))

print(random.choice(rl))
