class Digit:
    def __init__(self, value):
        self._value = value
    
    def value(self):
        return self._value

    def substitute(self, bindings):
        return self

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.value() == other.value()
        else:
            return False
        

class Variable:
    class Unbound:
        _count = -1
        
        @staticmethod
        def name():
            Variable.Unbound._count += 1
            return "$%s" % Variable.Unbound._count

    def __init__(self, name = None):
        if not name:
            name = Variable.Unbound.name()
        self._name = name
    
    def name(self):
        return self._name

    def substitute(self, bindings):
        if self.name() in bindings:
            return Digit(bindings[self.name()])
        return self

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name() == other.name()
        else:
            return False

class Operator:
    def __init__(self, left, right):
        self._left = left
        self._right = right
        
    def left(self):
        return self._left

    def right(self):
        return self._right

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.left() == other.left() and self.right() == other.right()
        return False

class Plus(Operator):
    def __init__(self, left, right):
        Operator.__init__(self, left, right)

    def substitute(self, bindings):
        return Plus(self.left().substitute(bindings), self.right().substitute(bindings))

class Minus(Operator):
    def __init__(self, left, right):
        Operator.__init__(self, left, right)

    def substitute(self, bindings):
        return Minus(self.left().substitute(bindings), self.right().substitute(bindings))

if __name__ == '__main__':
    assert Variable() != None

    assert Variable('A') == Variable('A')
    assert not Variable('A') == Variable('B')
    assert not Variable('A') == Variable()
    assert not Variable() == Variable()

    assert Plus(Variable('A'), Variable('B')) != None

    assert Plus(Variable('A'), Variable('B')) == Plus(Variable('A'), Variable('B'))
    assert not Plus(Variable('A'), Variable('B')) == Plus(Variable('A'), Variable())

    assert Minus(Variable('A'), Variable('B')) == Minus(Variable('A'), Variable('B'))
    assert not Minus(Variable('A'), Variable('B')) == Minus(Variable('A'), Variable())
    assert not Minus(Variable('A'), Variable('B')) == Plus(Variable('A'), Variable('B'))

    assert not Plus(Variable(),Variable()) == Variable()
    assert not Variable() == Plus(Variable(),Variable())
    assert not Minus(Variable(),Variable()) == Variable()
    assert not Variable() == Minus(Variable(),Variable())

    assert Digit(0) != None
    
    assert Digit(0) == Digit(0)
    assert not Digit(0) == Digit(1)

    assert Minus(Variable('A'), Variable('B')).substitute({'A': 0}) == Minus(Digit(0), Variable('B'))
    assert Plus(Digit(0), Variable('B')).substitute({'B': 1}) == Plus(Digit(0), Digit(1))
    assert Plus(Variable('A'), Variable('B')).substitute({'A': 0, 'B': 1}) == Plus(Digit(0), Digit(1))
    assert Minus(Variable('A'), Variable('A')).substitute({'A': 0}) == Minus(Digit(0), Digit(0))
