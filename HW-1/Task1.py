# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 
# n = int(input("Введите трехзначное число: "))
# a = n // 100
# b = n // 10 % 10
# c = n % 10
# print (f'Сумма чисел в веденном вами числе равна {a + b + c}')

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое 
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# sum = int(input("Всего сделано журавликов: "))
# P = S = sum // 4
# K = sum // 2
# print (f'Петя сделал {P}, Сережа сделал {S}, Катя сделала {K}')

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и 
# получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, 
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

# s = str(input('Введите шесть чисел вашего билета: '))
# sum1 = int(s[0]) + int(s[1]) + int(s[2])
# sum2 = int(s[3]) + int(s[4]) +int(s[5])
# if sum1 == sum2:
#   print('Ваш билет счастливый')
# else:
#   print('Ваш билет обычный')

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку 
# на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

# n = int(input())
# m = int(input())
# k = int(input())

# if k < m * n and (k % m == 0 or k % n == 0):
#     print('YES')
# else:
#     print('NO')