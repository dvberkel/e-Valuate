import unittest

from evaluate.expression.expression import *

class testExpression(unittest.TestCase):
    def testVariableEquality(self):
        self.assertEquals(Variable('A'), Variable('A'))
        self.assertNotEquals(Variable('A'), Variable('B'))
        self.assertNotEquals(Variable('A'), Variable())
        self.assertNotEquals(Variable(), Variable())

    def testPlusEquility(self):
        self.assertEquals(Plus(Variable('A'), Variable('B')),Plus(Variable('A'), Variable('B')))
        self.assertNotEquals(Plus(Variable('A'), Variable('B')),Plus(Variable('A'), Variable()))

    def testMinusEquility(self):
        self.assertEquals(Minus(Variable('A'), Variable('B')),Minus(Variable('A'), Variable('B')))
        self.assertNotEquals(Minus(Variable('A'), Variable('B')),Minus(Variable('A'), Variable()))

    def testMultiplyEquility(self):
        self.assertEquals(Multiply(Variable('A'), Variable('B')),Multiply(Variable('A'), Variable('B')))
        self.assertNotEquals(Multiply(Variable('A'), Variable('B')),Multiply(Variable('A'), Variable()))

    def testNumberEquility(self):
        self.assertEquals(Number(0),Number(0))
        self.assertNotEquals(Number(0),Number(1))

    def testExpressionEquality(self):
        self.assertNotEquals(Plus(Variable(),Variable()),Variable())
        self.assertNotEquals(Variable(),Plus(Variable(),Variable()))
        self.assertNotEquals(Plus(Variable(),Variable()),Number(0))
        self.assertNotEquals(Number(0),Plus(Variable(),Variable()))
        self.assertNotEquals(Number(0),Variable())
        self.assertNotEquals(Variable(),Number(0))

    def testSubstitution(self):
        self.assertEquals(Minus(Number(0), Variable('B')), Minus(Variable('A'), Variable('B')).substitute({'A': 0}))
        self.assertEquals(Minus(Number(0), Number(1)), Minus(Number(0), Variable('B')).substitute({'B': 1}))

    def testValueOfABoundExpression(self):
        self.assertEquals(0, Number(0).value())
        self.assertEquals(3, Plus(Number(1),Number(2)).value())
        self.assertEquals(-1, Minus(Number(1),Number(2)).value())
        self.assertEquals(6,  Multiply(Number(2),Number(3)).value())

    def testVariables(self):
        self.assertEquals(set([Variable('A'), Variable('B')]), Plus(Variable('A'), Variable('B')).variables())
        

if __name__ == '__main__':
    unittest.main()
