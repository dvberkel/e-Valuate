class IdentityEvaluator:
    def value(self, data):
        return data


if __name__ == '__main__':
    assert IdentityEvaluator().value(0) == 0
