# 2. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
# проходящей через эти точки.

a1 = int(input("Введите первую координату точки А: "))
a2 = int(input("Введите вторую координату точки А: "))

b1 = -2 * a1 + 1
b2 = -2 * a2 + 1

print(f'Прямая проходит через точки A({a1}, {a2}) и B({b1}, {b2})')