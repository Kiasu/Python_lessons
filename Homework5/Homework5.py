# Задача 1. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов. Это не просто сумма всех коэффициентов. Сумма многочленов равна многочлену, членами которого являются все члены данных многочленов.
'''

def GenTerms(coef: int, pow: int) -> str:
    if pow == 0:
        return f"{coef}"
    elif pow == 1:
        return f"{coef}*x"
    else:
        return f"{coef}*x^{pow}"


def DecPolynome(polyStr: str) -> dict:
    listTerms = polyStr.split(" = ")[0].split(" + ")
    dicrTerms = {}
    for term in listTerms:
        if "^" in term:
            tmp = term.split("^")
            dicrTerms[int(tmp[1])] = int(tmp[0].split("*")[0])
        elif "*" in term:
            dicrTerms[1] = int(term.split("*")[0])
        else:
            dicrTerms[0] = int(term)
    return dicrTerms


def EncPolynome(polyDict: dict) -> str:
    pow = list(polyDict.keys())
    pow.sort()
    pow.reverse()
    terms = []
    for p in pow:
        terms.append(GenTerms(polyDict[p], p))
    return " + ".join(terms) + " = 0"


def SumPolynome(poly1: dict, poly2: dict) -> dict:
    pow = set(poly1.keys()) | set(poly2.keys())
    result = {}
    for p in pow:
        result[p] = (poly1[p] if p in poly1 else 0) + \
            (poly2[p] if p in poly2 else 0)
    return result


try:
    with open(r"Homework\Homework5\polynomial1.txt", "r") as f:
        polyStr1 = f.readline()
    with open(r"Homework\Homework5\polynomial2.txt", "r") as f:
        polyStr2 = f.readline()
except:
    print("Failed to write file")
    exit()

print(polyStr1)
print(polyStr2)
polynom1 = DecPolynome(polyStr1)
polynom2 = DecPolynome(polyStr2)
sumPolynome = SumPolynome(polynom1, polynom2)
sumPolyStr = EncPolynome(sumPolynome)
print(sumPolyStr)

try:
    with open(r"Homework\Homework5\sumpolynomial.txt", "w") as f:
        f.write(sumPolyStr)
except:
    print("Failed to write file")
    exit()
'''

# Задача 2. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
'''
def GetRange(data: list) -> list:
    minValue = min(data)
    maxValue = max(data)
    items = set(data)
    if len(items) == maxValue-minValue+1:
        return [(minValue, maxValue)]
    else:
        result = []
        notItems = list({n for n in range(minValue, maxValue)} - items)
        notItems.sort()
        for a in notItems:
            sequence = {n for n in items if n < a}
            if len(sequence) > 1:
                result.append((min(sequence), max(sequence)))
            items = items - sequence
        return result


test1 = [1, 5, 2, 3, 4, 6, 1, 7]
test2 = [1, 5, 2, 3, 4, 1, 7]
test3 = [1, 5, 2, 3, 4, 1, 7, 8, 9, 11, 15, 20, 16, 18, 17, 23, 21]
print(test1, end=" -> ")
print(GetRange(test1))
print(test2, end=" -> ")
print(GetRange(test2))
print(test3, end=" -> ")
print(GetRange(test3))

'''
