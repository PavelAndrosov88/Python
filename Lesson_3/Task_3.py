# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

# import random

# N = int(input('Введите кол-во элементов в массиве: '))
# X = int(input('Введите число X: '))
# list = []

# for i in range(N):
#     list.append(random.randint(1, N))
# print(list) 

# sum = 0 
# for i in list:
#     if i == X:
#         sum += 1
# print(f'{X} встречается {sum} раз')

#  Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5  

# import random

# N = int(input('Введите кол-во элементов в массиве: '))
# X = int(input('Введите число X: '))
# list = []

# for i in range(N):
#     list.append(random.randint(1, N))
# print(list) 

# element = list[0]
# elementX = abs(list[0] - X)

# for i in list:
#     if abs(i - X) < elementX and X != i:
#         elementX = abs(i - X) 
#         element = i

# print(element)        

# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка;
# B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# *Пример:*

# ноутбук
#     12

# S = input('Введите слово: ')
# SL = {1 : 'AEIOULNSTRАВЕИНОРСТ', 2: 'DGДКЛМПУ', 3: 'BCMPБГЁЬЯ', 4: 'FHVWYЙЫ', 5: 'KЖЗХЦЧ', 8: 'JXШЭЮ', 10: 'QZФЩЪ'}
# sum = 0

# for i in S:
#     for j in SL:
#         if i.upper() in SL[j]:
#             sum += j
# print(sum)            