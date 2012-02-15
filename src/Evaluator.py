class IdentityEvaluator:
    def value(self, data):
        return data

class OppositeEvaluator:
    def __init__(self, evaluator):
        self._evaluator = evaluator

    def value(self, data):
        return -1 * self._evaluator.value(data)

if __name__ == '__main__':
    identity = IdentityEvaluator()
    assert identity.value(0) == 0
    assert identity.value(1) == 1

    opposite = OppositeEvaluator(identity)
    assert opposite.value(0) == 0
    assert opposite.value(1) == -1
