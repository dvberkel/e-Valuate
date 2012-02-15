from Tree import Tree

class GameTree(Tree):
    def __init__(self, data = None):
        Tree.__init__(self,data)
        self._value = None

    def evaluate(self, evaluator):
        if (not self._value):
            if (self.hasChildren()):
                self._value = max([-value for value in [child.evaluate(evaluator) for child in self.children()]])
            else:
                self._value = evaluator.value(self.data())
        return self._value

if __name__ == '__main__':
    assert GameTree() != None

    root = GameTree(0)
    assert root.data() == 0

    child = GameTree(1)
    root.addChild(child)
    assert child in root.children()

    identity = Evaluator:IdentityEvaluator()
    assert GameTree(0).evaluate(identity) == 0
    assert GameTree(1).evaluate(identity) == 1

    root = GameTree(0)
    root.addChild(GameTree(-1))
    root.addChild(GameTree(-2))
    assert root.evaluate(identity) == 2
