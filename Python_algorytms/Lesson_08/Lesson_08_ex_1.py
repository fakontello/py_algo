# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?

graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0]
]

# n * (n - 1) / 2

b = 0
for i in range(len(graph)):
    # длину графа умножить на количество единиц в одном элементе и разделить на два
    b = int(((i + 1) * i) / 2)

print(f'Количетво рукопожатий для 4 друзей равно {b}')
