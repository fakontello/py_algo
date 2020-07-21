# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random
from collections import deque
import sys

a = deque([random.randint(-5000, 5000) for _ in range(8)])
current_max_number = a[0]
current_min_number = a[-1]
print(a)

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
# 632
