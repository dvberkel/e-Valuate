from AlphaBetaTree import AlphaBetaTree
from Expression import *

class EvaluateTree:
    @staticmethod
    def createWith(expression, domain):
        tree = ProposeTree(expression, domain)
        return tree

class ProposeTree(AlphaBetaTree):
    def __init__(self, expression, domain):
        AlphaBetaTree.__init__(self, expression)
        if expression.variables():
            for proposal in domain:
                self.addChild(SubstituteTree(expression, domain, proposal))

class SubstituteTree(AlphaBetaTree):
    def __init__(self, expression, domain, proposal):
        AlphaBetaTree.__init__(self, proposal)
        for variable in expression.variables():
            self.addChild(ProposeTree(expression.substitute({variable.name(): proposal}), domain))

if __name__ == '__main__':
    from Tree import Tree
    assert EvaluateTree.createWith(Minus(Variable('A'),Variable('B')), [0, 1, 2]) != None

    root = Tree(Variable('A'))
    root.addChild(Tree(0).addChild(Tree(Number(0))))
    assert EvaluateTree.createWith(Variable('A'), [0]) == root

    root = Tree(Variable('A'))
    root.addChild(Tree(0).addChild(Tree(Number(0))))
    root.addChild(Tree(1).addChild(Tree(Number(1))))
    assert EvaluateTree.createWith(Variable('A'), [0,1]) == root
