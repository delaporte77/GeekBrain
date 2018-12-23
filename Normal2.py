'''
Created on Dec 23, 2018

@author: delaporte
'''


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    
    newList = []

    for i in range(len(origin_list)):
        newList.append(min(origin_list))
        origin_list.remove(min(origin_list))
    
    return newList

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))