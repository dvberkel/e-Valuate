from GameTree import GameTree
from decimal import Decimal

class AlphaBetaTree(GameTree):
    def __init__(self, data = None):
        GameTree.__init__(self, data)
    
    def evaluate(self, evaluator):
        return self.alphaBeta(evaluator)
    
    def alphaBeta(self, evaluator, alpha = -Decimal('infinity'), beta = Decimal('infinity')):
        if (self.hasChildren()):
            for child in self.children():
                alpha = max(alpha, - child.alphaBeta(OppositeTo(evaluator), -beta, -alpha))
                if (beta <= alpha):
                    break                            
            return alpha
        return evaluator.value(self.data())

if __name__ == '__main__':
    import Evaluator

    assert AlphaBetaTree() != None
 
    identity = Evaluator.IdentityEvaluator()
    assert AlphaBetaTree(0).evaluate(identity) == 0
    assert AlphaBetaTree(1).evaluate(identity) == 1

    left = GameTree(0)
    left.addChild(GameTree(1))
    left.addChild(GameTree(2))
    assert left.evaluate(identity) == 2

    right = GameTree(0)
    right.addChild(GameTree(-1))
    right.addChild(GameTree(-3))
    assert right.evaluate(identity) == -1

    root = GameTree(0)
    root.addChild(left)
    root.addChild(right)
    assert root.evaluate(identity) == 1
