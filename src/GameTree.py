from Tree import Tree

class GameTree(Tree):
    def __init__(self, data = None):
        Tree.__init__(self,data)

    def evaluate(self, evaluator):
        if (len(self.children()) > 0):
            return max([-value for value in [child.evaluate(evaluator) for child in self.children()]])
        return evaluator.value(self.data())

class IdentityEvaluator:
    def value(self, data):
        return data

if __name__ == '__main__':
    assert GameTree() != None

    root = GameTree(0)
    assert root.data() == 0

    child = GameTree(1)
    root.addChild(child)
    assert child in root.children()

    assert GameTree(0).evaluate(IdentityEvaluator()) == 0
    assert GameTree(1).evaluate(IdentityEvaluator()) == 1

    root = GameTree(0)
    root.addChild(GameTree(-1))
    root.addChild(GameTree(-2))
    assert root.evaluate(IdentityEvaluator()) == 2
