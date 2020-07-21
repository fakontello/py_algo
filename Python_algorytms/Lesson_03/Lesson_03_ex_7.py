# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.
import random

a = [random.randint(-50, 50) for _ in range(30)]
true_min = a[0]
second_min = a[0]
print(a)

for number in a:
    if true_min <= number < second_min:
        second_min = number
    elif number < true_min:
        second_min = true_min
        true_min = number

print(f'Два наименьших числа массива: {true_min}, {second_min}.')
