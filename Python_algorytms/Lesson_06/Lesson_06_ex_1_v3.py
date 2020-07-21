# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random
import sys
import os

b = tuple(random.randint(-5000, 5000) for _ in range(8))
current_max_number = b[0]
current_min_number = b[-1]
print(b)
a = list(b)
print(sys.getsizeof(b))
for number in a:
    if number > current_max_number:
        current_max_number = number
    if number < current_min_number:
        current_min_number = number

minn = a.index(current_min_number)
maxx = a.index(current_max_number)
a[minn], a[maxx] = a[maxx], a[minn]

print(a)
print(sys.getsizeof(a))
print(sys.version, sys.platform)
# 112
# Кортеж требует меньше оперативной памяти, нежели очередь или список.
