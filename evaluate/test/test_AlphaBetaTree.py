import unittest

from evaluate.AlphaBetaTree import AlphaBetaTree
from evaluate.GameTree import GameTree
from evaluate.Evaluator import IdentityEvaluator

class testAlphaBetaTree(unittest.TestCase):
    def testAlphaBetaTreeIsAGameTree(self):
        root = AlphaBetaTree()

        actual = isinstance(root, GameTree)

        self.assertTrue(actual)

    def testEvaluationOfAlphaBetaTree(self):
        root = AlphaBetaTree()
        root.addChild(AlphaBetaTree(0).addChild(AlphaBetaTree(1)).addChild(AlphaBetaTree(2)))
        root.addChild(AlphaBetaTree(0).addChild(AlphaBetaTree(-1)).addChild(AlphaBetaTree(-3)))

        actual = root.evaluate(IdentityEvaluator())

        self.assertEquals(1, actual)

if __name__ == '__main__':
    unittest.main()
