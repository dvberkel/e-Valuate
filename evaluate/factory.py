from evaluate.expression import *
import re

class Token:
    variable = re.compile("^\\w+")
    number = re.compile("^\\d+")
    operator = re.compile("^(\+|-|\*)")
    leftBracket = re.compile("^\(")
    rightBracket = re.compile("^\)")
    whitespace = re.compile("^\\s+")

    @staticmethod
    def next(expression):
        for regex in [Token.number, Token.variable, Token.operator, Token.whitespace, Token.leftBracket, Token.rightBracket]:
            m = regex.match(expression)
            if m:
                return m
        if expression == '':
            return None
        raise Exception("unrecognized expression", expression)

class Rpn:
    operatorFactory = {'+': (lambda x,y: Plus(x,y)), '-': (lambda x,y: Minus(x,y)), '*': (lambda x,y: Multiply(x,y))}

    def __init__(self,expression):
        self.expression = expression

    def create(self):
        parts = self.expression.split(" ")
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
    
    def create(self):
        return Rpn(self.toRpn()).create()

    def toRpn(self):
        result, stack = [], []
        for token in Tokenize(self._expression):
            if Token.number.match(token) or Token.variable.match(token):
                result.append(token)
            elif Token.leftBracket.match(token):
                stack.append(token)
            elif Token.rightBracket.match(token):
                while len(stack) > 0 and not Token.leftBracket.match(stack[-1]):
                    result.append(stack.pop())
                stack.pop()
            elif Token.operator.match(token):
                while len(stack) > 0 and self._lessPrecedence(token, stack[-1]):
                    result.append(stack.pop())
                stack.append(token)
        while len(stack) > 0:
            result.append(stack.pop())
        return " ".join(result)

    def _lessPrecedence(self, o1, o2):
        if (o1 == '+' or o1 == '+'):
            if (o2 == '*'):
                return True
        return False        

class Tokenize:
    def __init__(self, expression):
        self.tokens = self._tokenize(expression)
        self.index = 0

    def _tokenize(self, expression):
        index, tokens = 0, []
        m = Token.next(expression[index:])
        while m:
            index += m.end()
            if not Token.whitespace.match(m.group()):
                tokens.append(m.group())
            m = Token.next(expression[index:])
    
        return tokens

    def __iter__(self):
        return self

    def next(self):
        if self.index == len(self.tokens):
            raise StopIteration
        else:
            token = self.tokens[self.index]
            self.index += 1
            return token

if __name__ == '__main__':
    assert Rpn("A B -").create() == Minus(Variable('A'), Variable('B'))
    assert Rpn("A B +").create() == Plus(Variable('A'), Variable('B'))
    assert Rpn("A B *").create() == Multiply(Variable('A'), Variable('B'))

    assert Rpn("A B - C D - *").create() == Multiply(Minus(Variable('A'), Variable('B')), Minus(Variable('C'), Variable('D')))
    assert Rpn("A B - C 5 - *").create() == Multiply(Minus(Variable('A'), Variable('B')), Minus(Variable('C'), Number(5)))

    assert Infix("A + B").toRpn() == "A B +"
    assert Infix("A * B + C").toRpn() == "A B * C +"
    assert Infix("A * B + C * D").toRpn() == "A B * C D * +"

    assert Infix("A * (B + C)").toRpn() == "A B C + *"

    assert Infix("(A - B) * (C - 5)").create() == Multiply(Minus(Variable('A'), Variable('B')), Minus(Variable('C'), Number(5)))
