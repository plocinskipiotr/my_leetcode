TEST_INPUT = \
    [
        ('()', True),
        ('(]', False),
        ('()[]{}', True),
        ('[[(({}))]}', False),
        ('(])', False)
    ]


def load_test_input():
    return TEST_INPUT
