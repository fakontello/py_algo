# 7. Определить, является ли год, который ввел пользователь, високосным или не високосным.

year = int(input("Ведите год: "))
if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print("Год является невисокосным")
else:
    print("Это високосный год")
