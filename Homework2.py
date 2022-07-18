
# Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
'''
try:
    num = float(input("Input number: "))

except:
    print("Need input number")
    exit()

def SumDigits(n):
    digits = int(str(n).replace('.', ''))

    sum = 0
    while digits != 0:
        sum += digits % 10
        digits //= 10
    return sum

print(SumDigits(num))

'''

# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
'''
from unittest import result


try:
    N = int(input('Input integer number: '))
except:
    print('Need input integer number')
    exit()


def GetSequence(num):
    result = []

    for i in range(1, num+1):
        if i > 1:
            result.append(result[-1] * i)
        else:
            result.append(i)
    return result

print(GetSequence(N))

'''
