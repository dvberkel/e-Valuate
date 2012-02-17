from evaluate.tree import Tree
from evaluate.evaluator import OppositeTo

class GameTree(Tree):
    def __init__(self, data = None):
        Tree.__init__(self,data)

    def evaluate(self, evaluator):
        if (self.hasChildren()):
            return max([-value for value in [child.evaluate(OppositeTo(evaluator)) for child in self.children()]])
        return evaluator.value(self.data())

if __name__ == '__main__':
    import Evaluator

    assert GameTree() != None

    root = GameTree(0)
    assert root.data() == 0

    child = GameTree(1)
    root.addChild(child)
    assert child in root.children()

    identity = Evaluator.IdentityEvaluator()
    assert GameTree(0).evaluate(identity) == 0
    assert GameTree(1).evaluate(identity) == 1

    root = GameTree(0).addChild(GameTree(1)).addChild(GameTree(2))
    assert root.evaluate(identity) == 2

    left = GameTree(0).addChild(GameTree(1)).addChild(GameTree(2))
    assert left.evaluate(identity) == 2

    right = GameTree(0).addChild(GameTree(-1)).addChild(GameTree(-3))
    assert right.evaluate(identity) == -1

    root = GameTree(0).addChild(left).addChild(right)
    assert root.evaluate(identity) == 1
    
