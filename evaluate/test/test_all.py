import unittest

from evaluate.tree.test.tree import testTree
from evaluate.tree.test.game import testGameTree
from evaluate.tree.test.alphabeta import testAlphaBetaTree
from evaluate.expression.test.expression import testExpression
from evaluate.tree.test.evaluated import testEvaluateTree
from evaluate.expression.test.factory import testExpressionFactory

class EvaluateSuite(unittest.TestSuite):
    def __init__(self):
        unittest.TestSuite.__init__(self)
        for clazz in [testTree, testGameTree, testAlphaBetaTree, testExpression, testEvaluateTree, testExpressionFactory]:
            self.addTest(unittest.makeSuite(clazz))

if __name__ == '__main__':
    suite = EvaluateSuite()

    unittest.TextTestRunner().run(suite)
