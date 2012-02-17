import unittest

from evaluate.EvaluateTree import EvaluateTree, Evaluator
from evaluate.AlphaBetaTree import AlphaBetaTree
from evaluate.Expression import *

class testEvaluateTree(unittest.TestCase):
    def testEvaluateTreeIsAnAlphaBetaTree(self):
        self.assertTrue(isinstance(EvaluateTree.createWith(Minus(Variable('A'),Variable('B')), [0,1]), AlphaBetaTree))

    def testEvaluation(self):
        evaluator = Evaluator()
        self.assertEquals(0, EvaluateTree.createWith(Minus(Variable('A'),Variable('B')), [0]).alphaBeta(evaluator))
        self.assertEquals(0, EvaluateTree.createWith(Minus(Variable('A'),Variable('B')), [0, 1]).alphaBeta(evaluator))
        self.assertEquals(1, EvaluateTree.createWith(Minus(Variable('A'),Variable('B')), [0, 1, 2]).alphaBeta(evaluator))
        self.assertEquals(1, EvaluateTree.createWith(Minus(Variable('A'),Variable('B')), [0, 1, 2, 3]).alphaBeta(evaluator))
        

if __name__ == '__main__':
    unittest.main()
