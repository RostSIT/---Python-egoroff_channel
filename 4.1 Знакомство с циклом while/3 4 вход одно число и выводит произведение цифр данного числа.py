"""
4.2 Обход всех цифр числа с помощью while
2 из 4 шагов пройдено
1 из 3 баллов  получен
Программа принимает на вход одно натуральное число и выводит на экран произведение цифр данного числа

Sample Input 1:

415
Sample Output 1:

20
Sample Input 2:

102
Sample Output 2:

0
"""


a = int(input())
c = 1
while a > 0:
    b = a % 10
    c *= b
    a = a // 10
print(c)
