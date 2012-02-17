import unittest

from evaluate.Tree import Tree

class testTree(unittest.TestCase):

    def testDefaultDataIsNone(self):
        tree = Tree()

        actual = tree.data()

        self.assertEquals(None, actual)

    def testDataIsStored(self):
        expected = 1
        tree = Tree(expected)
        
        actual = tree.data()

        self.assertEquals(expected,actual)

    def testDefaultNoChildren(self):
        tree = Tree()

        actual = tree.hasChildren()
        
        self.assertFalse(actual)

    def testAddingAChildDoesMakeAChild(self):
        tree = Tree().addChild(Tree())

        actual = tree.hasChildren()

        self.assertTrue(actual)

    def testChildIsInChildren(self):
        tree, child = Tree(), Tree()
        tree.addChild(child)

        actual = (child in tree.children())

        self.assertTrue(actual)

    def testEquality(self):
        self.assertEquals(Tree(), Tree())
        self.assertNotEqual(Tree().addChild(Tree()), Tree())
        self.assertNotEqual(Tree().addChild(Tree()), Tree().addChild(Tree(0)))

if __name__ == '__main__':
    unittest.main()
