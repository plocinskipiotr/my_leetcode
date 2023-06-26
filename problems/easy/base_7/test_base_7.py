from unittest import TestCase
from base_7 import Solution


class TestSolution(TestCase):
    def test_convert_to_base7(self):
        s = Solution()
        x = s.convertToBase7(100)
        self.assertEqual(x, '202')

    def test_convert_to_base7_2(self):
        s = Solution()
        x = s.convertToBase7(7)
        self.assertEqual(x, '10')

    def test_convert_to_base7_3(self):
        s = Solution()
        x = s.convertToBase7(-7)
        self.assertEqual(x, '-10')

    def test_convert_to_base7_4(self):
        s = Solution()
        x = s.convertToBase7(0)
        self.assertEqual(x, '0')
