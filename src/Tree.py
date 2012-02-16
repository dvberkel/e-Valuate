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
