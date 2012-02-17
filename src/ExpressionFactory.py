from Expression import *
import re

class Token:
    variable = re.compile("^\\w+")
    number = re.compile("^\\d+")
    operator = re.compile("^(\+|-|\*)")
    whitespace = re.compile("^\\s+")

    @staticmethod
    def next(expression):
        for regex in [Token.number, Token.variable, Token.operator, Token.whitespace]:
            m = regex.match(expression)
            if m:
                return m
        return None

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

class Infix:
    def __init__(self, expression):
        self._expression = expression

    def toRpn(self):
        index, result, stack, tokens = 0, [], [],  self._tokenize()
        while index < len(tokens):
            token = tokens[index]
            if Token.number.match(token) or Token.variable.match(token):
                result.append(token)
            elif Token.operator.match(token):
                stack.append(token)
            index += 1
        while len(stack) > 0:
            result.append(stack.pop())
        return " ".join(result)

    def _tokenize(self):
        index, tokens = 0, []
        m = Token.next(self._expression[index:])
        while m:
            index += m.end()
            if not Token.whitespace.match(m.group()):
                tokens.append(m.group())
            m = Token.next(self._expression[index:])
    
        return tokens


if __name__ == '__main__':
    assert Rpn.create("A B -") == Minus(Variable('A'), Variable('B'))
    assert Rpn.create("A B +") == Plus(Variable('A'), Variable('B'))
    assert Rpn.create("A B *") == Multiply(Variable('A'), Variable('B'))

    assert Rpn.create("A B - C D - *") == Multiply(Minus(Variable('A'), Variable('B')), Minus(Variable('C'), Variable('D')))
    assert Rpn.create("A B - C 5 - *") == Multiply(Minus(Variable('A'), Variable('B')), Minus(Variable('C'), Number(5)))

    assert Infix("A + B").toRpn() == "A B +"
