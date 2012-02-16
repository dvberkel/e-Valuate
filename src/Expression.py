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
        if type(other) is type(self):
            return self.name() == other.name()
        else:
            return False

if __name__ == '__main__':
    assert Variable() != None

    assert Variable('A') == Variable('A')
    assert not Variable('A') == Variable('B')
    assert not Variable('A') == Variable()
    assert not Variable() == Variable()
