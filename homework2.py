#для проверки - разкомментировать!
"""
Задача 10: 
На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
а некоторые – гербом. Определите минимальное число монеток, которые нужно 
перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть
"""

# n = int(input("Введите число монеток: "))
# count = 0
# count_mon=0
# for i in range(n):
#     temp = int(input(f"Введите строну {count_mon+1} монетки (1-орел, 0 - решка): "))
#     if temp == 1:
#         count += 1
#     count_mon += 1
# if count >= n/2:
#     print (n - count)
# else: print(count) 

#__________________________________________________________________________
"""
Задача 12: 
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.
"""

# sum = int(input("Input a sum of natural number"))
# mult = int(input("Input a product of numbers "))
# first_num = 0
# second_num = 0 
# temp = 0
# for i in range(sum):
#     if sum-(sum-temp) == mult/(sum-temp):
#         first_num = temp
#         second_num = sum - temp
#         print(f"First number is {first_num}")
#         print(f"Second number is {second_num}")
#         break
#     temp += 1

# if first_num == second_num == 0:
#     print("Incorrect sum or product. Please try again with new numbers")

#__________________________________________________________________________
"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа
вида 2k), не превосходящие числа N.
"""


# n = int(input("Input the last number: "))
# count = 0
# pow = 2
# while pow < n:
#     pow = 2**count
#     if pow>n:
#         break
#     else: print(pow, end=" ")
#     count += 1


    
