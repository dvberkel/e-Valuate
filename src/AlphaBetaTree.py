from GameTree import GameTree
from decimal import Decimal

class AlphaBetaTree(GameTree):
    def __init__(self, data = None):
        GameTree.__init__(self, data)
    
    def evaluate(self, evaluator):
        result, alpha, beta = self.alphaBeta(evaluator) 
        return result
    
    def alphaBeta(self, evaluator, alpha = -Decimal('infinity'), beta = Decimal('infinity')):
        return GameTree.evaluate(self,evaluator), alpha, beta

if __name__ == '__main__':
    import Evaluator

    assert AlphaBetaTree() != None
 
    identity = Evaluator.IdentityEvaluator()
    assert AlphaBetaTree(0).evaluate(identity) == 0
    assert AlphaBetaTree(1).evaluate(identity) == 1
