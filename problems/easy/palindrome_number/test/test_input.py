TEST_INPUT = \
    [
        (-101, False),
        (-1, False),
        (0, True),
        (1, True),
        (10, False),
        (101, True),
        (1000, False),
        (123321, True),
        (1234321, True)
    ]


def load_test_input():
    return TEST_INPUT
