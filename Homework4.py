# Задача 1. Вычислить результат деления двух чисел c заданной точностью d
'''
from math import log10


def CalcPi(acc: float) -> float:
    pi = 0
    pi_pr = 1
    k = 0
    while abs(pi_pr - pi) > acc:
        pi_pr = pi
        pi += (4/(8*k+1) - 2/(8*k+4) - 1/(8*k+5) - 1/(8*k+6)) / (16**k)
        k += 1
    return round(pi, -int(log10(accuracy)))


try:
    accuracy = float(input("Input accuracy 1e-10 до 1e-1: "))
    if (accuracy < 1e-10 or accuracy > 1e-1):
        raise
except:
    print("Invalid input")
else:
    print(CalcPi(accuracy))

'''

# Задача 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N. 3 (необязательное). 
'''
def GetPrimeFactors(n: int) -> list:
    result = []
    factor = 2
    while(n > 1):
        if(n % factor == 0):
            result.append(factor)
            n //= factor
        else:
            factor += 1
    return result

try:
    n = int(input("Input natural number: "))
    if (n < 1):
        raise
except:
    print("Need input natural number")
else:
    print(GetPrimeFactors(n))

'''





