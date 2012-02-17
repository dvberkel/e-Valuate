import unittest

from evaluate.test.test_Tree import testTree
from evaluate.test.test_GameTree import testGameTree
from evaluate.test.test_AlphaBetaTree import testAlphaBetaTree
from evaluate.test.test_Expression import testExpression
from evaluate.test.test_EvaluateTree import testEvaluateTree

class EvaluateSuite(unittest.TestSuite):
    def __init__(self):
        unittest.TestSuite.__init__(self)
        for clazz in [testTree, testGameTree, testAlphaBetaTree, testExpression, testEvaluateTree]:
            self.addTest(unittest.makeSuite(clazz))

if __name__ == '__main__':
    suite = EvaluateSuite()

    unittest.TextTestRunner().run(suite)
