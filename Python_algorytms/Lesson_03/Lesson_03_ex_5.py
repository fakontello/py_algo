# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random

a = [random.randint(-50, 50) for _ in range(20)]
current_min_number = a[0]
print(a)

for number in a:
    if number < current_min_number:
        current_min_number = number

print(f'Максимальный отрицательный элемент {current_min_number}, его позиция в массиве {a.index(current_min_number)}')
