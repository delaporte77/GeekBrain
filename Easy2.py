'''
Created on Dec 23, 2018

@author: delaporte
'''


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    
    x = 0
    number_part1 = 0
    number_part2 = 0
    
    for i in str(ticket_number):
        if x < 3:
            number_part1 += int(i)
            x += 1
        else:
            number_part2 += int(i)
            
    if number_part1 == number_part2:
        return True
        


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))