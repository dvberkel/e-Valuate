import unittest

from evaluate.ExpressionFactory import *
from evaluate.Expression import *

class testExpressionFactory(unittest.TestCase):
    def testRpnCreate(self):
        self.assertEquals(Minus(Variable('A'),Variable('B')), Rpn("A B -").create())
        self.assertEquals(Minus(Variable('A'), Multiply(Number(5),Variable('B'))), Rpn("A 5 B * -").create())

    def testInfixToRpn(self):
        self.assertEquals("A B -", Infix("A - B").toRpn())
        self.assertEquals("A B +", Infix("A + B").toRpn())
        self.assertEquals("A B * C D * +", Infix("A * B + C * D").toRpn())

    def testInfixCreate(self):
        self.assertEquals(Minus(Variable('A'),Variable('B')), Infix("A - B").create())
        self.assertEquals(Minus(Variable('A'), Multiply(Number(5),Variable('B'))), Infix("A - 5 * B").create())

if __name__ == '__main__':
    unittest.main()
