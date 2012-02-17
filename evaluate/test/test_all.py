import unittest

from evaluate.test.test_Tree import testTree
from evaluate.test.test_GameTree import testGameTree
from evaluate.test.test_AlphaBetaTree import testAlphaBetaTree
from evaluate.test.test_Expression import testExpression


class EvaluateSuite(unittest.TestSuite):
    def __init__(self):
        unittest.TestSuite.__init__(self)
        self.addTest(unittest.makeSuite(testTree))
        self.addTest(unittest.makeSuite(testGameTree))
        self.addTest(unittest.makeSuite(testAlphaBetaTree))
        self.addTest(unittest.makeSuite(testExpression))

if __name__ == '__main__':
    suite = EvaluateSuite()

    unittest.TextTestRunner().run(suite)
