# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого — цифры числа.
from collections import deque


first = deque(input())
second = deque(input())
third = deque()

list_of_16numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']

# умножение

# a = 0
# a1 = 0
# b = 0
#
# for i in second, first:
#     a = list_of_16numbers.index(second[-1]) * list_of_16numbers.index(first[-1])
#     if a > 16:
#         b = a - a // 16 * 16
#         b = list_of_16numbers[b]
#         a1 = a // 16
#     if a < 16:
#         b = list_of_16numbers[a]

j = -1
k = 0
for i in second:
    one = list_of_16numbers.index(i)
    two = list_of_16numbers.index(second[j])
    third.append(list_of_16numbers[(one + two + k) % 16])
    if (one + two) >= 15:
        k = 1
    else:
        k = 0
        j -= 1
    if j == -len(second)-1:
        break

diff = len(first) - len(second)

first = list(first)
second = list(second)
third = list(third)

if diff:
    for i in second[-diff:]:
        third.append(list_of_16numbers[(list_of_16numbers.index(first[-diff]) + k) % 16])
        if list_of_16numbers.index(first[-diff]) + 1 >= 15:
            k = 1
        else:
            k = 0

if k == 1:
    third.append('1')

print(third)
