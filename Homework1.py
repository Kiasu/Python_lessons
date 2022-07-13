# Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
'''
try:
    dayNumber = int(input('Input day number: '))
except:
    print('Нужно было ввести целое число!')
    exit()


def DayIsAWeekend(dayNumber):
    return dayNumber == 6 or dayNumber == 7

def DayIsAWorkingDay(dayNumber):
    return 1 <= dayNumber <= 55

        

if DayIsAWeekend(dayNumber):
    print('Weekend')
elif DayIsAWorkingDay(dayNumber):
    print('Working Day')
else:
    print('It is not day of the week')

'''

# Задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости.
'''
try:
    x = float(input('Coordinate x: '))
    y = float(input('Coordinate y: '))
except:
    print('Need input number')
    exit()

def GetQuarter(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    else:
        return 0


def Axis(x, y):
    if x == 0 and y == 0:
        return 'X и Y'
    elif x == 0:
        return 'Y'
    elif y == 0:
        return 'X'
    else:
        return ''


quart = GetQuarter(x, y)
if quart != 0:
    print(f'Dot ({x}, {y}) on the quart {quart}')
else:
    print(f'Dot ({x}, {y}) on the axis {Axis(x, y)}')
    
'''