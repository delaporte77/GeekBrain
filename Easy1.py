'''
Created on Dec 23, 2018

@author: delaporte
'''

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    
    ndigits = int('1' + '0' * ndigits)
    number = number * ndigits
    
    if float(number) - int(number) >= 0.5:
        number += 1
    
    return float(int(number) / ndigits)
    
    

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))