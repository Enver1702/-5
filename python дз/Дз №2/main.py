"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток,
которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, 
которые нужно перевернуть
"""
"""
n = int(input('введите количество монет : '))
count1 = 0
count2 = 0
for i in range(n):
    x = int(input(f' {i+1}-ая монета: '))
    if x == 0:
        count1 += 1
    if x == 1:
        count2 += 1
else: 
     if count2 < count1:
      print(count2)
     else:
      print(count1)  
"""

  
"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.
"""
"""
s = int(input('сумму двух чисел : '))
p = int(input('произведение двух чисел : '))
for x in range(s):
    for y in range(p):
        if s == x + y and p == x * y:
            print(x,y)
            
"""
"""
# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
n = int(input('Введи число n: '))
i = 0
while 2 ** i <= n:
    print(i , 2**i)
    i += 1
"""