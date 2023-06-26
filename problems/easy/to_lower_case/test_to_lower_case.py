from unittest import TestCase
from to_lower_case import Solution


class TestSolution(TestCase):
    def test_to_lower_case(self):
        s = Solution()
        data = 'Data'
        x = s.toLowerCase(data)
        self.assertEqual('data', x)

    def test_to_lower_case2(self):
        s = Solution()
        data = '"al&phaBET"'
        x = s.toLowerCase(data)
        self.assertEqual('"al&phabet"', x)
