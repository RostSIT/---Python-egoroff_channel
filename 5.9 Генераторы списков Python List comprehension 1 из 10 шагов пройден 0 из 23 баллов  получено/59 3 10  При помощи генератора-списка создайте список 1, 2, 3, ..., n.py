"""5.9 Генераторы списков Python | List comprehension 2 из 10 шагов пройдено 2 из 23 баллов  получено При помощи
генератора-списка создайте список [1, 2, 3, ..., n], само натуральное число n будет поступать на вход вашей программе.

В качестве ответа просто выведите получившийся список

Sample Input 1:

1
Sample Output 1:

[1]
Sample Input 2:

5
Sample Output 2:

[1, 2, 3, 4, 5]
Sample Input 3:

9
Sample Output 3:

[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

n = int(input())
a = [i + 1 for i in range(n)]
print(a)
