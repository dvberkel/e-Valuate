class Tree:
    def __init__(self, data = None):
        self._data = data
        self._children = []

    def data(self):
        return self._data

    def children(self):
        return self._children

    def hasChildren(self):
        return len(self.children()) > 0

    def addChild(self, child):
        self._children.append(child)
        return self
    
    def __eq__(self, other):
        if isinstance(other, Tree):
            if (self.data() == other.data()):
                ownChildren = self.children()
                otherChildren = other.children()
                if (len(ownChildren) == len(otherChildren)):
                    for index in range(len(ownChildren)):
                        if not (ownChildren[index] == otherChildren[index]):
                            return False                            
                    return True
        return False

    def __str__(self):
        return "{{{0} [{1}]}}".format(str(self.data()), ", ".join(map(lambda x: str(x), self.children())))
        
if __name__ == '__main__':
    assert Tree() != None

    assert Tree().data() == None
    assert Tree(1).data() == 1

    assert len(Tree().children()) == 0
    assert not Tree().hasChildren()
    
    root, child = Tree(), Tree()
    root.addChild(child)
    assert child in root.children()
    assert root.hasChildren()

    assert len(Tree().addChild(Tree()).children()) == 1

    assert Tree(0) == Tree(0)
    assert not Tree(0) == Tree(1)
    assert not Tree(0).addChild(Tree(0)) == Tree(0)
    assert not Tree(0).addChild(Tree(0)) == Tree(0).addChild(Tree(1))
