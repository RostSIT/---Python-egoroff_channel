"""5.3 Цикл for. Обход списков и строк 1 из 8 шагов пройден 0 из 28 баллов  получено Заполняем список Ваша задача
создать список из n строк. Программа сперва будет принимать натуральное число n, а затем n строк в каждой отдельной
строке. В качестве ответа выведите получившийся список.

Sample Input 1:

4
Джон
Пол
Ринго
Джордж
Sample Output 1:

['Джон', 'Пол', 'Ринго', 'Джордж']
Sample Input 2:

2
black
white
Sample Output 2:

['black', 'white']
"""

b = []
a = int(input())
for i in range(a):
    s = input()
    b.append(s)
print(b)
