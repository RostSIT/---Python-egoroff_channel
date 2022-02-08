"""
5.7 Вложенные списки, Часть 2
5 из 7 шагов пройдено
29 из 46 баллов  получено
Спираль

Требуется вывести квадрат, состоящий из N×N клеток, заполненных числами от 1 до N2 по спирали (см. примеры).

Входные данные
Программа получает на вход одно число n.

Выходные данные Программа должна вывести матрицу, заполненную числами от 1 до N2 по спирали, при этом между числами
может быть любое количество пробелов. Не допускается начинать спираль в ином, кроме верхнего левого, углу,
закручивать спираль против часовой стрелки или изнутри наружу.

Разбор задачи

Sample Input:

3
Sample Output:

1 2 3
8 9 4
7 6 5
"""

n = int(input())
mas = [[0] * n for i in range(n)]
i = 1
x = 0
y = -1
d_row = 0
d_column = 1
length = len(str(n ** 2))
while i <= n ** 2:
    if 0 <= x + d_row < n and 0 <= y + d_column < n and mas[x + d_row][y + d_column] == 0:
        x += d_row
        y += d_column
        mas[x][y] = i
        i += 1
    else:
        if d_column == 1:
            d_column = 0
            d_row = 1
        elif d_row == 1:
            d_row = 0
            d_column = -1
        elif d_column == -1:
            d_column = 0
            d_row = -1
        elif d_row == -1:
            d_row = 0
            d_column = 1
for row in mas:
    for elem in row:
        print(str(elem).rjust(length), end=' ')
    print()
