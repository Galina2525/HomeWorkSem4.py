# Задайте натуральное число N (от 1 и более). Напишите программу, которая составит
# список простых множителей(делится без остатка только на себя и единицу) числа N 
# (факторизация целых чисел)

#num = int(input('Введите число: '))   
# def primfacs(n):
#    i = 2
#    primfac = []
#    while i * i <= n:
#        while n % i == 0:
#            primfac.append(i)
#            n = n //i
#        i = i + 1
#    if n > 1:
#        primfac.append(n)
#    return primfac     
# print(primfacs(num))   

import math

number=int(input('Введите число: '))

for i in range(2, int(math.sqrt(number)) + 1): # обычно делитель не будет больше корня
    while (number % i == 0): # while, а не if
        print(i)
        number //= i # убираем множитель из числа

if (number != 1): # но один делитель может быть больше корня
    print (number)
    