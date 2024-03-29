from evaluate.tree.alphabeta import AlphaBetaTree
from evaluate.expression import *

class EvaluateTree(AlphaBetaTree):
    @staticmethod
    def createWith(expression, domain):
        tree = ProposeTree(expression, domain)
        return tree

class ProposeTree(EvaluateTree):
    def __init__(self, expression, domain):
        EvaluateTree.__init__(self, expression)
        if expression.variables():
            for proposal in domain:
                self.addChild(SubstituteTree(expression, domain, proposal))

class SubstituteTree(EvaluateTree):
    def __init__(self, expression, domain, proposal):
        EvaluateTree.__init__(self, proposal)
        for variable in expression.variables():
            self.addChild(ProposeTree(expression.substitute({variable.name(): proposal}), domain))

class Evaluator:
    def value(self, expression):
        return expression.value()

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

    evaluator = Evaluator()
    assert EvaluateTree.createWith(Minus(Variable('A'), Variable('B')), [0]).alphaBeta(evaluator) == 0
    assert EvaluateTree.createWith(Minus(Variable('A'), Variable('B')), [0, 1]).alphaBeta(evaluator) == 0
    assert EvaluateTree.createWith(Minus(Variable('A'), Variable('B')), [0, 1, 2]).alphaBeta(evaluator) == 1
    assert EvaluateTree.createWith(Minus(Variable('A'), Variable('B')), [0, 1, 2, 3]).alphaBeta(evaluator) == 1
    assert EvaluateTree.createWith(Minus(Variable('A'), Variable('B')), [0, 1, 2, 3, 4]).alphaBeta(evaluator) == 2
