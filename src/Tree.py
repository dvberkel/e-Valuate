class Tree:
    def __init__(self, data = None):
        self._data = data

    def data(self):
        return self._data

if __name__ == '__main__':
    assert Tree() != None

    assert Tree().data() == None
    assert Tree(1).data() == 1
