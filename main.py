"""
Калькулятор обратно польской нотации
"""
import operator
import sys
import math

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

def infix_to_postfix(expression):
    """
    Преобразование инфиксного выражения в обратную польскую нотацию.

    :param expression: строка с инфиксным выражением
    :return: выражение с обратно польской нотацией
    """
    stack = []
    output = []
    tokens = expression.split()

    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                raise ValueError("Неверный формат выражения!")
        else:
            while (stack and stack[-1] != '('
                   and ((token != '^' and PRIORITY.get(token, 0) <= PRIORITY.get(stack[-1], 0))
                        or (token == '^' and PRIORITY.get(token, 0) < PRIORITY.get(stack[-1], 0)))):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        if stack[-1] == '(':
            raise ValueError("Неверный формат выражения!")
        output.append(stack.pop())

    return ' '.join(output)


def polska(st):
    """
    Считывает обратно польскую запись и считает выражение.

    :param st: выражение обратно польской записи
    :return: результат
    """

    stack = []
    lst = st.split()
    lst_copy = lst.copy()

    digits_count = 0
    operators_count = 0

    try:
        for i in lst_copy:
            if i.isdigit():
                stack.append(int(i))
                lst.remove(i)
                digits_count += 1
            else:
                cnt1, cnt2 = stack.pop(), stack.pop()
                result = OPERATORS[i](cnt2, cnt1)
                if result == float('inf') or math.isnan(result):
                    raise ValueError

                stack.append(result)
                lst.remove(i)
                operators_count += 1
        result = stack.pop()
    except Exception as exc:
        raise ValueError("Неверный формат выражения!") from exc

    if digits_count != operators_count + 1:
        raise ValueError("Неверный формат выражения!")

    return result


def main():
    """
    Реализация калькулятора обратно польской записи
    """
    while True:
        exp = input("Введите выражение: ")

        if not exp:
            print("Калькулятор закрывается ...")
            sys.exit(0)

        try:
            polska_exp = infix_to_postfix(exp)
        except ValueError:
            print("Введено неверное выражение!")
            print("Попробуйте еще раз ... ")
            continue

        print("Ваша обратно польская нотация:", polska_exp)

        try:
            res = polska(polska_exp)
        except ValueError:
            print("Введено неверное выражение!")
            print("Попробуйте еще раз ... ")
            continue

        print("Результат:", res)


if __name__ == "__main__":
    main()
