#
# 5.6 Вложенные списки
# 6 из 16 шагов пройдено
# 25 из 87 баллов  получено
# A. Красивая матрица
#
# Перед Вами матрица размера 5 × 5, состоящая из 24-x нулей и единственной единицы. Строки матрицы пронумеруем числами
# от 1 до 5 сверху вниз, столбцы матрицы пронумеруем числами от 1 до 5 слева направо. За один ход разрешается применить
# к матрице одно из двух следующих преобразований:
#
# Поменять местами две соседние строки матрицы, то есть строки с номерами i и i + 1 для некоторого целого i (
# 1 ≤ i < 5). Поменять местами два соседних столбца матрицы, то есть столбцы с номерами j и j + 1 для некоторого целого
# j (1 ≤ j < 5). Вы считаете, что матрица будет выглядеть красиво, если единственная единица этой матрицы будет
# находиться в ее центре (в клетке, которая находится на пересечении третьей строки и третьего столбца). Посчитайте,
# какое минимальное количество ходов потребуется, чтобы сделать матрицу красивой.
#
# Входные данные
#
# Входные данные состоят из пяти строк, в каждой из которых записаны пять целых чисел: j-ое число в i-ой строке входных
# данных обозначает элемент матрицы, стоящий на пересечении i-ой строки и j-ого столбца. Гарантируется, что матрица
# состоит из 24-x нулей и единственной единицы.
#
# Выходные данные
#
# Выведите единственное целое число — минимальное количество действий, которое требуется,
# чтобы сделать матрицу красивой.
#
# Решение задачи Youtube Patreon Boosty
#
# Sample Input 1:
#
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# Sample Output 1:
#
# 2
# Sample Input 2:
#
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 1 0 0
# 0 0 0 0 0
# Sample Output 2:
#
# 1


a = []
for i in range(5):
    a.append(list(map(int, input().split())))
for i in range(5):
    for j in range(5):
        if a[i][j] == 1:
            row = i
            column = j

print(abs(2 - row) + abs(2 - column))

