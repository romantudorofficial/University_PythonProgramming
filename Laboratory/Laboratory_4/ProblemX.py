def eval_expr (expr):

    operands = set()
    numbers = []
    number = 0

    prio = {'+' : (1, lambda a,b: a+b),
            '-' : (1, lambda a,b: a-b),
            '*' : (1, lambda a,b: a*b),
            '/' : (1, lambda a,b: a/b)}

    for char in expr:
        if char not in "0123456789":
            operands.append(char)
            numbers.append(number)
            number = 0
        else:
            number = number * 10 + int(char)

    numbers.append(number)

    for i in range(len(operands)):


    while (len(numbers) != 1):
        op1 = operands[-1]
        op2 = operands[-2]
        if prio[op1][0] == prio[op2][0]:
            value = prio[op1][1](numbers[op1], numbers[op2])
            numbers[-2] = value
            numbers.pop[-3]
            operands.pop(-2)

        elif prio[op2][0] == op1.number:
            value = prio[op2][1](numbers[op1], numbers[op2])
            numbers[-2] = value
            numbers.pop(-3)
            operands.pop(-2)

    return prio[operands[0][1](numbers[0], numbers[1])]



print(eval("4+17-9*2+16/4"))
print(eval_expr("4+17-9*2+16/4"))