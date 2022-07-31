# Задача 1. Создайте программу для игры в "Крестики-нолики".
'''
import random

EPMTY = 0
X = 1
O = -1
SYMBOLS = {EPMTY: "-", X: "X", O: "O"}

X_WIN = X
O_WIN = O
DRAW = 0
NOT_END = -2


def CheckBoard(brd):
    winCombinationX = (X, X, X)
    winCombinationO = (O, O, O)
    combinations = tuple(map(tuple, [brd[0:3], brd[3:6], brd[6:9],
                                     brd[0:9:3], brd[1:9:3], brd[2:9:3],
                                     brd[0:9:4], brd[-3:-8:-2]]))
    if winCombinationX in combinations:
        return X_WIN
    elif winCombinationO in combinations:
        return O_WIN
    elif EPMTY in brd:
        return NOT_END
    else:
        return DRAW


def PrintBoard(brd: list):
    print(" ".join(map(lambda i: SYMBOLS[i], brd[0:3])))
    print(" ".join(map(lambda i: SYMBOLS[i], brd[3:6])))
    print(" ".join(map(lambda i: SYMBOLS[i], brd[6:9])))


def HumanMove(brd: list):
    while True:
        try:
            m = input("Make a move (row column by space): ")
            i, j = list(map(int, m.split()))
            move = (i-1)*3 + (j-1)
            if brd[move] != EPMTY:
                raise
        except:
            print("Incorrect")
        else:
            return move


def OneMoveWin(brd: list, moves: set, wMove: int) -> int:
    for move in moves:
        newBrd = brd[::]
        newBrd[move] = wMove
        if CheckBoard(newBrd) == wMove:
            return move
    return -1


def TwoMoveWin(brd: list, priorityMoves: set, allMoves: set, wMove: int) -> int:
    for firstMove in priorityMoves:
        newBrd = brd[::]
        newBrd[firstMove] = wMove
        for secondMove in allMoves - {firstMove}:
            newBrdSecond = newBrd[::]
            newBrdSecond[secondMove] = wMove
            if CheckBoard(newBrdSecond) == wMove:
                return firstMove
    return -1


def BotMove(brd: list):
    possibleMoves = {m for m, s in enumerate(brd) if s == EPMTY}
    cornerСellsEmpty = possibleMoves & {0, 2, 6, 8}
    sideСellsEmpty = possibleMoves & {1, 3, 5, 7}
    center = 4
    move = OneMoveWin(brd, possibleMoves, O)
    if move != -1:
        return move
    move = OneMoveWin(brd, possibleMoves, X)
    if move != -1:
        return move
    if brd[center] == EPMTY:
        return center
    else:
        if len(cornerСellsEmpty) == 2 and ((brd[0] == X and brd[8] == X) or (brd[2] == X and brd[6] == X)):
            move = TwoMoveWin(brd, sideСellsEmpty, possibleMoves, O)
            if move != -1:
                return move
    move = TwoMoveWin(brd, cornerСellsEmpty, possibleMoves, O)
    if move != -1:
        return move
    move = TwoMoveWin(brd, possibleMoves, possibleMoves, O)
    if move != -1:
        return move
    if len(cornerСellsEmpty) != 0:
        return random.choice(tuple(cornerСellsEmpty))
    return random.choice(tuple(possibleMoves))


board = [EPMTY, EPMTY, EPMTY,
         EPMTY, EPMTY, EPMTY,
         EPMTY, EPMTY, EPMTY]

whoseMove = random.randint(0, 1)
if whoseMove != X:
    print("First turn X")
else:
    print("First turn O")
gameState = NOT_END
PrintBoard(board)
while gameState == NOT_END:
    whoseMove = (whoseMove + 1) % 2
    if whoseMove == X:
        print("Turn X")
        move = HumanMove(board)
        board[move] = X
    else:
        print("Turn O")
        move = BotMove(board)
        board[move] = O
    PrintBoard(board)
    print("-----------------")
    gameState = CheckBoard(board)

if gameState == X_WIN:
    print("You win!")
elif gameState == O_WIN:
    print("You win!")
else:
    print("Draw!!!")

'''

# Задача 2. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,. приоритет операций стандартный.
'''
def ConvertRPN(inputSequence: list) -> list:
    operatorsPriority = {'+': 1, '-': 1, '/': 2, '*': 2}
    outputSequence = []
    stack = []
    for token in inputSequence:
        if token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                outputSequence.append(stack.pop())
            stack.pop()
        elif token in operatorsPriority.keys():
            while len(stack) > 0 and stack[-1] in operatorsPriority.keys():
                if operatorsPriority[stack[-1]] >= operatorsPriority[token]:
                    outputSequence.append(stack.pop())
                else:
                    break
            stack.append(token)
        else:
            outputSequence.append(token)

    while len(stack) > 0:
        outputSequence.append(stack.pop())

    return outputSequence


def CalcRPN(rpnSequence: list) -> float:
    operators = {'+': lambda a, b: a + b,
                 '-': lambda a, b: a - b,
                 '/': lambda a, b: a / b,
                 '*': lambda a, b: a * b}
    stack = []
    for token in rpnSequence:
        if token in operators.keys():
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(operators[token](operand1, operand2))
        else:
            stack.append(float(token))
    return stack[0]

def Calculator(eval: str):
    operators = {'+', '-', '/', '*', '(', ')'}
    for o in operators:
        eval = eval.replace(o, f' {o} ')
    tokens = eval.split()
    rpn = ConvertRPN(tokens)
    return CalcRPN(rpn)


test0 = "(1+6)*2+4"
test1 = "2+4*3"
test2 = "(6+2)*8"
test3 = "1-1*3"
test4 = "(5*(6+3)/(15-9.8))*2.5"
test5 = "(1+2+1)*3"
print(f"{test0} = {Calculator(test0)}")
print(f"{test1} = {Calculator(test1)}")
print(f"{test2} = {Calculator(test2)}")
print(f"{test3} = {Calculator(test3)}")
print(f"{test4} = {Calculator(test4)}")
print(f"{test5} = {Calculator(test5)}")

'''

# Задача 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
'''
def RLEEncode(text: str) -> str:
    encodeText = []
    startIndex = 0
    endIndex = 1
    while startIndex < len(text):
        while endIndex < len(text) and text[startIndex] == text[endIndex]:
            endIndex += 1
        if endIndex - startIndex > 3:
            encodeText.extend(
                ["#", chr(endIndex-startIndex), text[startIndex]])
        else:
            encodeText.extend(list(text[startIndex:endIndex]))
        startIndex = endIndex
        endIndex = startIndex + 1
    return "".join(encodeText)


def RLEDecode(encodeText: str) -> str:
    decodeText = []
    startIndex = 0
    while startIndex < len(encodeText):
        if encodeText[startIndex] == "#":
            decodeText.extend([encodeText[startIndex+2]] *
                              ord(encodeText[startIndex+1]))
            startIndex += 3
        else:
            decodeText.append(encodeText[startIndex])
            startIndex += 1
    return "".join(decodeText)


try:
    with open(r"Homework\Homework6\testdata.txt", "r", encoding="utf-8") as file:
        data = file.readline()
except:
    print("Failed to upload file")
    exit()
else:
    print("The original data has been uploaded")
    print(data)
    print("-------------------------------------")

encode = RLEEncode(data)
print("Coding")
print(encode)
try:
    with open(r"Homework\Homework6\encodingdata.txt", "w", encoding="utf-8") as file:
        file.write(encode)
except:
    print("Failed to upload file")
    exit()
else:
    print("The encoded data is recorded")
    print("-------------------------------------")

try:
    with open(r"Homework\Homework6\encodingdata.txt", "r", encoding="utf-8") as file:
        encodeData = file.readline()
except:
    print("Failed to upload file")
    exit()
else:
    print("The encoded data is loaded")
    print(encodeData)
    print("-------------------------------------")

decodeData = RLEDecode(encodeData)
print("Decoding")
print(decodeData)
try:
    with open(r"Homework\Homework6\decodingdata.txt", "w", encoding="utf-8") as file:
        file.write(decodeData)
except:
    print("Failed to upload file")
    exit()
else:
    print("Decoded data is recorded")
    print("-------------------------------------")

'''