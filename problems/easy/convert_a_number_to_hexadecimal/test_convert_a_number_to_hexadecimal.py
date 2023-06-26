from unittest import TestCase
from convert_a_number_to_hexadecimal import Solution


class TestSolution(TestCase):
    def test_to_hex(self):
        s = Solution()
        data = 255
        self.assertEqual('ff', s.toHex(data))

        data = -1
        self.assertEqual('ffffffff', s.toHex(data))