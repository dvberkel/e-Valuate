from Expression import *
import re

class Token:
    variable = re.compile("^\\w+")
    number = re.compile("^\\d+")
    operator = re.compile("^(\+|-|\*)")

class Rpn:
    operatorFactory = {'+': (lambda x,y: Plus(x,y)), '-': (lambda x,y: Minus(x,y)), '*': (lambda x,y: Multiply(x,y))}

    @staticmethod
    def create(rpnExpression):
        parts = rpnExpression.split(" ")
        stack = []
        index = 0
        while index < len(parts):
            token = parts[index]
            if Token.number.match(token):
                stack.append(Number(int(token,10)))
            elif Token.variable.match(token):
                stack.append(Variable(token))
            elif Token.operator.match(token):
                right = stack.pop()
                left = stack.pop()
                factory = Rpn.operatorFactory[token]
                stack.append(factory(left, right))
            index += 1
        return stack[0]

if __name__ == '__main__':
    assert Rpn.create("A B -") == Minus(Variable('A'), Variable('B'))
    assert Rpn.create("A B +") == Plus(Variable('A'), Variable('B'))
    assert Rpn.create("A B *") == Multiply(Variable('A'), Variable('B'))

    assert Rpn.create("A B - C D - *") == Multiply(Minus(Variable('A'), Variable('B')), Minus(Variable('C'), Variable('D')))
    assert Rpn.create("A B - C 5 - *") == Multiply(Minus(Variable('A'), Variable('B')), Minus(Variable('C'), Number(5)))
