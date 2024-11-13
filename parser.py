from abc import ABC
from numpy import double
from abc import ABC, abstractmethod


class Expression(ABC):
    @abstractmethod
    def calc(self) -> double:
        pass


# implement the classes here
class BinExp(Expression):
    def __init__(self, right:Expression, left:Expression):
        self.right = right
        self.left = left


class Num(Expression):
    def __init__(self, n):
        super().__init__()
        self.num = n

    def calc(self) -> double:
        return self.num


class Plus(BinExp):
    def __init__(self, n1:Expression, n2:Expression):
        super().__init__(n1, n2)

    def calc(self) -> double:
        return self.right.calc() + self.left.calc()


class Minus(BinExp):
    def __init__(self, n1: Expression, n2: Expression):
        super().__init__(n1, n2)

    def calc(self) -> double:
        return self.right.calc() - self.left.calc()


class Mul(BinExp):
    def __init__(self, n1:Expression, n2:Expression):
        super().__init__(n1, n2)

    def calc(self) -> double:
        return self.right.calc() * self.left.calc()


class Div(BinExp):
    def __init__(self, n1:Expression, n2:Expression):
        super().__init__(n1, n2)

    def calc(self) -> double:
        return self.right.calc() / self.left.calc()



# implement the parser function here
def isDigit(c) -> bool:
    return '0' <= c <= '9'


def infixToPostfix(expression):
    expression = expression.replace("(-", "(0-")
    priorities = {
        "+": 2,
        "-": 2,
        "*": 3,
        "/": 3
    }
    classes = {
        "+": Plus,
        "-": Minus,
        "*": Mul,
        "/": Div
    }
    buffer = ''
    queue = []
    stack = []

    for char in expression:
        if isDigit(char):
            buffer += char
        elif char =='(':
            if buffer != '':
                queue.append(int(buffer))
                buffer = ''
            stack.append('(')
        elif char == ')':
            if buffer != '':
                queue.append(int(buffer))
                buffer = ''
            while len(stack) > 0 and stack[-1] != '(':
                queue.append(classes[stack.pop()])
            if stack and stack[-1] == '(':
                stack.pop()
        else:
            if buffer != '':
                queue.append(int(buffer))
                buffer = ''
            while len(stack) > 0 and stack[-1] != '(' and priorities[char] <= priorities[stack[-1]]:
                queue.append(classes[stack.pop()])
            stack.append(char)
    while len(stack) > 0:
        if stack[-1] != '(':
            queue.append(classes[stack.pop()])
        else:
            stack.pop()

    return queue


def parser(expression) -> double:
    queue = infixToPostfix(expression)
    orderedStack = []
    while len(queue) > 0:
        if isinstance(queue[0], int):
            orderedStack.insert(0,Num(queue.pop(0)))
        else:
            sec = orderedStack.pop(0)
            if len(orderedStack) > 0:
                first = orderedStack.pop(0)
            else:
                first = Num(0)
            exp: Expression = (queue.pop(0))(first, sec)
            orderedStack.insert(0,Num(exp.calc()))
    return orderedStack[0].calc()
