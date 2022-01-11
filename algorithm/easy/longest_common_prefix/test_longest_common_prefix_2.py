from unittest import TestCase
from longest_common_prefix_2 import Solution


class TestSolution(TestCase):

    def test_longest_common_prefix_00(self):
        data = ['x', '']
        s = Solution()
        r = s.longestCommonPrefix(data)
        self.assertEqual(r, '')

    def test_longest_common_prefix_01(self):
        data = ['x']
        s = Solution()
        r = s.longestCommonPrefix(data)
        self.assertEqual(r, 'x')

    def test_longest_common_prefix_02(self):
        data = ['x','x','y']
        s = Solution()
        r = s.longestCommonPrefix(data)
        self.assertEqual(r, '')

    def test_longest_common_prefix_0(self):
        data = ['x', 'x']
        s = Solution()
        r = s.longestCommonPrefix(data)
        self.assertEqual(r, 'x')

    def test_longest_common_prefix_1(self):
        data = ['xy', 'xxy']
        s = Solution()
        r = s.longestCommonPrefix(data)
        self.assertEqual(r, 'x')

    def test_longest_common_prefix_2(self):
        data = ['xxy', 'xxy']
        s = Solution()
        r = s.longestCommonPrefix(data)
        self.assertEqual(r, 'xxy')

    def test_longest_common_prefix_3(self):
        data = ['xxy', 'xxxy']
        s = Solution()
        r = s.longestCommonPrefix(data)
        self.assertEqual(r, 'xx')

    def test_longest_common_prefix_4(self):
        data = ['xxxy', 'xxxy']
        s = Solution()
        r = s.longestCommonPrefix(data)
        self.assertEqual(r, 'xxxy')

    def test_longest_common_prefix_5(self):
        data = ['', 'xxxy', 'xxxxy']
        s = Solution()
        r = s.longestCommonPrefix(data)
        self.assertEqual(r, '')

    def test_longest_common_prefix_6(self):
        data = ['x', 'xxxy', 'xxxxy']
        s = Solution()
        r = s.longestCommonPrefix(data)
        self.assertEqual(r, 'x')

    def test_longest_common_prefix_7(self):
        data = ['xxy', 'xxxy', 'xxxxy']
        s = Solution()
        r = s.longestCommonPrefix(data)
        self.assertEqual(r, 'xx')

    def test_longest_common_prefix_8(self):
        data = ['xxxxy', 'xxxxy', 'xxxxy']
        s = Solution()
        r = s.longestCommonPrefix(data)
        self.assertEqual(r, 'xxxxy')

    def test_longest_common_prefix_9(self):
        data = ['xxxxxy', 'xxxxy', 'xxxy', 'xxy']
        s = Solution()
        r = s.longestCommonPrefix(data)
        self.assertEqual(r, 'xx')

    def test_longest_common_prefix_10(self):
        data = ['xxxxxy', 'xxxxy', 'x', 'xxy', 'xxxy']
        s = Solution()
        r = s.longestCommonPrefix(data)
        self.assertEqual(r, 'x')

    def test_longest_common_prefix_11(self):
        data = ['']
        s = Solution()
        r = s.longestCommonPrefix(data)
        self.assertEqual(r, '')

    def test_longest_common_prefix_12(self):
        data = ['xx', 'xx', 'xx', 'xx']
        s = Solution()
        r = s.longestCommonPrefix(data)
        self.assertEqual(r, 'xx')

    def test_longest_common_prefix_13(self):
        data = ['xxx', 'xxx', 'xxx', 'xxx']
        s = Solution()
        r = s.longestCommonPrefix(data)
        self.assertEqual(r, 'xxx')

    def test_longest_common_prefix_14(self):
        data = ['xxx', 'x', 'xx', 'xxxx']
        s = Solution()
        r = s.longestCommonPrefix(data)
        self.assertEqual(r, 'x')

    def test_longest_common_prefix_15(self):
        data = ['xxx', 'xxx', 'xxx', 'xxxxxxx']
        s = Solution()
        r = s.longestCommonPrefix(data)
        self.assertEqual(r, 'xxx')

    def test_longest_common_prefix_16(self):
        data = ['xxyxx', 'xxyx', 'xxyx', 'xxyxx']
        s = Solution()
        r = s.longestCommonPrefix(data)
        self.assertEqual(r, 'xxyx')
