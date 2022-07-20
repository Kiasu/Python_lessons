# Задача 1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
'''
inpList = ["abc", "efg", "123", "over", "qwe",
             "ertqwe", "123", "ячс", "damage", "567"]

def FindNumber(inp: list):
    outp = []
    for item in inp:
        if item.isdigit():
            outp.append(item)
    return outp


outpList = FindNumber(inpList)
print(f"Checklist {inpList}", end = " ")

if len(outpList) > 0:
    print(f"Have a number {' '.join(outpList)}")
else:
    print("Dont have a number")
'''

# 2. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
'''
test = [
    (["qwe", "asd", "zxc", "qwe", "ertqwe"], "qwe"),
    (["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], "йцу"),
    (["йцу", "фыв", "ячс", "цук", "йцукен"], "йцу"),
    (["123", "234", 123, "567"], "123"),
    ([], "123")
]


def FindSecPos(input: list, findValue: str) -> int:
    count = 0
    for i in range(len(input)):
        if input[i] == findValue:
            count += 1
        if count == 2:
            return i
    return -1


for _ in test:
    secPos = FindSecPos(_[0], _[1])
    if secPos == -1:
        print(f"In list {_[0]} the second occurrence of the element {_[1]} dont have")
    else:
        print(f"In list {_[0]} the second occurrence of the element {_[1]}  - {secPos}")
'''