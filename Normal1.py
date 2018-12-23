'''
Created on Dec 23, 2018

@author: delaporte
'''


# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    
    fibo = [1, 1]
    
    for i in range(m-1):
        fibo.append(fibo[-2] + fibo[-1])
        
    return fibo[n:]
    
print(fibonacci(5, 8))