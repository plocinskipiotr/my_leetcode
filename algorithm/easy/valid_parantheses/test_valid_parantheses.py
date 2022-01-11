from unittest import TestCase

from valid_parantheses import Solution


class TestSolution(TestCase):
    def test_is_valid_00(self):
        s = Solution()
        data = ''
        r = s.isValid(data)
        self.assertTrue(r)

    def test_is_valid_0(self):
        s = Solution()
        data = '()'
        r = s.isValid(data)
        self.assertTrue(r)

    def test_is_valid_1(self):
        s = Solution()
        data = '[]'
        r = s.isValid(data)
        self.assertTrue(r)

    def test_is_valid_2(self):
        s = Solution()
        data = '{}'
        r = s.isValid(data)
        self.assertTrue(r)

    def test_is_valid_3(self):
        s = Solution()
        data = ')'
        r = s.isValid(data)
        self.assertFalse(r)

    def test_is_valid_33(self):
        s = Solution()
        data = '('
        r = s.isValid(data)
        self.assertFalse(r)

    def test_is_valid_4(self):
        s = Solution()
        data = '}'
        r = s.isValid(data)
        self.assertFalse(r)

    def test_is_valid_44(self):
        s = Solution()
        data = '{'
        r = s.isValid(data)
        self.assertFalse(r)

    def test_is_valid_5(self):
        s = Solution()
        data = ']'
        r = s.isValid(data)
        self.assertFalse(r)

    def test_is_valid_55(self):
        s = Solution()
        data = '['
        r = s.isValid(data)
        self.assertFalse(r)

    def test_is_valid_6(self):
        s = Solution()
        data = '()]'
        r = s.isValid(data)
        self.assertFalse(r)

    def test_is_valid_7(self):
        s = Solution()
        data = '([{}])'
        r = s.isValid(data)
        self.assertTrue(r)

    def test_is_valid_8(self):
        s = Solution()
        data = '([{}]]'
        r = s.isValid(data)
        self.assertFalse(r)

    def test_is_valid_9(self):
        s = Solution()
        data = '([{}])'
        r = s.isValid(data)
        self.assertTrue(r)
