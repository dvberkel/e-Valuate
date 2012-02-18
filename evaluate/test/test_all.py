import unittest

from evaluate.test.tree import testTree
from evaluate.test.game import testGameTree
from evaluate.test.alphabeta import testAlphaBetaTree
from evaluate.test.expression import testExpression
from evaluate.test.evaluated import testEvaluateTree
from evaluate.test.factory import testExpressionFactory

class EvaluateSuite(unittest.TestSuite):
    def __init__(self):
        unittest.TestSuite.__init__(self)
        for clazz in [testTree, testGameTree, testAlphaBetaTree, testExpression, testEvaluateTree, testExpressionFactory]:
            self.addTest(unittest.makeSuite(clazz))

if __name__ == '__main__':
    suite = EvaluateSuite()

    unittest.TextTestRunner().run(suite)
