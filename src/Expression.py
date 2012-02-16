class Expression:
    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self._eq(other)
        else:
            return False

class Number(Expression):
    def __init__(self, value):
        self._value = value
    
    def value(self):
        return self._value

    def substitute(self, bindings):
        return self

    def variables(self):
        return set([])

    def _eq(self,other):
        return self.value() == other.value()

    def __hash__(self):
        return hash(self.value())

    def __str__(self):
        return "{}".format(str(self.value()))

class Variable(Expression):
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
            return Number(bindings[self.name()])
        return self
    
    def variables(self):
        return set([self])

    def _eq(self,other):
        return self.name() == other.name()

    def __hash__(self):
        return hash(self.name())

    def __str__(self):
        return "{}".format(self.name())

class Operator(Expression):
    def __init__(self, left, right):
        self._left = left
        self._right = right
        
    def left(self):
        return self._left

    def right(self):
        return self._right

    def variables(self):
        return self.left().variables().union(self.right().variables())

    def _eq(self,other):
        return self.left() == other.left() and self.right() == other.right()
    
    def __hash__(self):
        return hash(self.left()) ^ hash(self.right())

    def __str__(self):
        return "({0} {2} {1})".format(str(self.left()), str(self.right()), self._symbol())

class Plus(Operator):
    def __init__(self, left, right):
        Operator.__init__(self, left, right)

    def substitute(self, bindings):
        return Plus(self.left().substitute(bindings), self.right().substitute(bindings))
    
    def value(self):
        return self.left().value() + self.right().value()

    def _symbol(self):
        return "+"

class Minus(Operator):
    def __init__(self, left, right):
        Operator.__init__(self, left, right)

    def substitute(self, bindings):
        return Minus(self.left().substitute(bindings), self.right().substitute(bindings))

    def value(self):
        return self.left().value() - self.right().value()

    def _symbol(self):
        return "-"

class Multiply(Operator):
    def __init__(self, left, right):
        Operator.__init__(self, left, right)

    def substitute(self, bindings):
        return Multiply(self.left().substitute(bindings), self.right().substitute(bindings))
    
    def value(self):
        return self.left().value() * self.right().value()

    def _symbol(self):
        return "*"

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

    assert Number(0) != None
    
    assert Number(0) == Number(0)
    assert not Number(0) == Number(1)

    assert Minus(Variable('A'), Variable('B')).substitute({'A': 0}) == Minus(Number(0), Variable('B'))
    assert Plus(Number(0), Variable('B')).substitute({'B': 1}) == Plus(Number(0), Number(1))
    assert Plus(Variable('A'), Variable('B')).substitute({'A': 0, 'B': 1}) == Plus(Number(0), Number(1))
    assert Minus(Variable('A'), Variable('A')).substitute({'A': 0}) == Minus(Number(0), Number(0))

    assert Multiply(Variable('A'), Variable('B')) != None

    assert Multiply(Variable('A'), Variable('B')).substitute({'A': 1}) == Multiply(Number(1), Variable('B'))

    assert Number(0).value() == 0
    assert Plus(Number(1),Number(2)).value() == 3
    assert Minus(Number(1),Number(2)).value() == -1
    assert Multiply(Number(2),Number(3)).value() == 6

    assert Plus(Variable('A'),Variable('B')).variables() == set([Variable('A'), Variable('B')])
