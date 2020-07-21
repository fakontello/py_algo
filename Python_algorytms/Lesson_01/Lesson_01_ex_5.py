# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

import string
a = list(string.ascii_lowercase)
b = input('Введите любое число от 0 до 26: ')
print(a[int(b)])
