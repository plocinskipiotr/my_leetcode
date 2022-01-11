from unittest import TestCase

from longest_common_prefix import Solution


class TestSolution(TestCase):
    def test_longest_common_prefix(self):
        s = Solution()

        data = ['xxxxxy', 'xxxxy']
        y = s.longestCommonPrefix(data)
        self.assertEqual(y, 'xxxx')

        data = ['xxxxy', 'xxxy']
        y = s.longestCommonPrefix(data)
        self.assertEqual(y, 'xxx')

        data = ['xxxxy', 'xxy']
        y = s.longestCommonPrefix(data)
        self.assertEqual(y, 'xx')

        data = ['xxxxy', 'xy']
        y = s.longestCommonPrefix(data)
        self.assertEqual(y, '')

        data = ['xxxxxy', 'xxxxy', 'xxy', 'xxxxx']
        y = s.longestCommonPrefix(data)
        self.assertEqual(y, 'xx')

        data = ['xxxxxxy', 'xxxxxy', 'xxxy', 'xxxxxxxxxxx']
        y = s.longestCommonPrefix(data)
        self.assertEqual(y, 'xxx')

        data = ['xxxxxxy', 'xxxxxy', 'xy', 'xxxxxxxxxxx']
        y = s.longestCommonPrefix(data)
        self.assertEqual(y, '')

        data = ['xxxxxxy', 'xxy', 'xxxxxy', 'xxxxxx']
        y = s.longestCommonPrefix(data)
        self.assertEqual(y, 'xx')

        data = ['xy', 'xy', 'xxxxxy', 'xxxxxx']
        y = s.longestCommonPrefix(data)
        self.assertEqual(y, '')
