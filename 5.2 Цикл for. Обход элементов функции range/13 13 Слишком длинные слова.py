"""
5.2 Цикл for. Обход элементов функции range
12 из 13 шагов пройдено
19 из 24 баллов  получено
Слишком длинные слова
Иногда некоторые слова вроде «civilization» или «internationalization» настолько длинны, что их весьма утомительно писать много раз в каком либо тексте.

Будем считать слово слишком длинным, если его длина строго больше 10 символов. Все слишком длинные слова можно заменить специальной аббревиатурой.

Эта аббревиатура строится следующим образом: записывается первая и последняя буква слова, а между ними — количество
букв между первой и последней буквой (в десятичной системе счисления и без ведущих нулей).

Таком образом, «civilization» запишется как «c10n», а «internationalization» как «i18n».

Вам предлагается автоматизировать процесс замены слов на аббревиатуры. При этом все слишком длинные слова должны быть
заменены аббревиатурой, а слова, не являющиеся слишком длинными, должны остаться без изменений.

Входные данные В первой строке содержится целое число n (1 ≤ n ≤ 100). В каждой из последующих n строк содержится по
одному слову. Все слова состоят из малых латинских букв и имеют длину от 1 до 100 символов.

Выходные данные
Выведите n строк. В i строке должен находиться результат замены i-го слова из входных данных.

Sample Input:

4
word
civilization
internationalization
pneumonoultramicroscopicsilicovolcanoconiosis
Sample Output:

word
c10n
i18n
p43s
"""

a = int(input())
word = []
for i in range(a):
    s = input()
    if len(s) > 10:
        word = [s[0], len(s)-2, s[-1]]
        print(s[0], len(s)-2, s[-1], sep='')
    else:
        print(s)
