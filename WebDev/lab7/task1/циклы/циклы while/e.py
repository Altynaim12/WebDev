
N = int(input())

# Инициализируем переменную для хранения значения k
k = 0

# Пока 2 в степени k меньше N, увеличиваем k на 1
while 2 ** k < N:
    k += 1

print(k)
