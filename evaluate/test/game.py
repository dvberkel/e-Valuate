import unittest

from evaluate.tree.game import GameTree
from evaluate.tree.tree import Tree
from evaluate.evaluator import IdentityEvaluator

class testGameTree(unittest.TestCase):
    def testGameTreeInstanceOfTree(self):
        root = GameTree()

        actual = isinstance(root, Tree)

        self.assertTrue(actual)

    def testEvaluationOfLeaf(self):
        expected = 0
        root, evaluator = GameTree(expected), IdentityEvaluator()

        actual = root.evaluate(evaluator)

        self.assertEquals(expected, actual)

    def testEvaluationOfTreeOfDepthOne(self):
        expected, lessThenExpected = 2, 1
        root = GameTree(lessThenExpected).addChild(GameTree(lessThenExpected)).addChild(GameTree(expected))
        evaluator = IdentityEvaluator()

        actual = root.evaluate(evaluator)

        self.assertEquals(expected, actual)

    def testEvaluationOfTreeOfDepthTwo(self):
        expected = 1
        left = GameTree(0).addChild(GameTree(1)).addChild(GameTree(2))
        right = GameTree(0).addChild(GameTree(-1)).addChild(GameTree(-3))
        root = GameTree(0).addChild(left).addChild(right)

        actual = root.evaluate(IdentityEvaluator())

        self.assertEquals(expected, actual)

if __name__ == '__main__':
    unittest.main()
