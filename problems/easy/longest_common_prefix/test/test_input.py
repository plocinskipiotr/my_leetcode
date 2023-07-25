TEST_INPUT = \
    [
        (['xxxxxy', 'xxxxy'], 'xxxx'),
        (['xxxxy', 'xxxy'], 'xxx'),
        (['xxxxy', 'xxy'], 'xx'),
        (['xxxxxy', 'xxxxy', 'xxy', 'xxxxx'], 'xx'),
        (['xxxxxxy', 'xxxxxy', 'xxxy', 'xxxxxxxxxxx'], 'xxx'),
        (['xxxxxxy', 'xxxxxy', 'xy', 'xxxxxxxxxxx'], ''),
        (['xxxxxxy', 'xxy', 'xxxxxy', 'xxxxxx'], ''),
        (['xy', 'xy', 'xxxxxy', 'xxxxxx'], ''),
    ]


def load_test_input():
    return TEST_INPUT
