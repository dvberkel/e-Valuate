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

class Minus(Operator):
    def __init__(self, left, right):
        Operator.__init__(self, left, right)

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
