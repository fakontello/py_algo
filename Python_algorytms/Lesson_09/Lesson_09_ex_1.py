# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
def substr(string):
    j = 1
    a = set()
    while True:
        for i in range(len(string)-j+1):
            a.add(string[i:i+j])
        if j == len(string) - 1:
            break
        j += 1

    a = list(a)
    a.sort(key=lambda x: len(x))

    return len(a)

print(substr('papa'))

#  python -m timeit -n 1000 -s "import Lesson_09_ex_1" "Lesson_09_ex_1.substr('papa')"
#  1000 loops, best of 5: 5.59 usec per loop
# new result: 1000 loops, best of 5: 11.2 nsec per loop
