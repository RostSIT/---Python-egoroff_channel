"""
6.5 Множества в Python. Тип данных set
3 из 11 шагов пройдено
2 из 24 баллов  получено
Напишите программу, которая выводит все цифры, встречающиеся в символьной строке больше одного раза.

Входные данные
Входная строка может содержать содержит цифры, пробелы и латинские буквы.

Выходные данные
Программа должна вывести в одну строчку в порядке возрастания все цифры, встречающиеся во входной строке больше одного раза. Если таких цифр нет, нужно вывести слово 'NO'.

Sample Input 1:

abc12cd34ef35
Sample Output 1:

3
Sample Input 2:

yrey424u3iou2315
Sample Output 2:

2 3 4
Sample Input 3:

qwerty123
Sample Output 3:

NO
"""

string = set(input())
a = set()
counter = 0
b = {}
for i in sorted(string):
    if i.isdigital:
        counter += 1
        b.setdefault(i, counter)

    s
