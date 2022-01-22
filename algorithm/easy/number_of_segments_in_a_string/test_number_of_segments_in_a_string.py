from unittest import TestCase
from number_of_segments_in_a_string import Solution


class TestSolution(TestCase):
    def test_count_segments(self):
        s = Solution()
        data = "Hello, my name is John a"
        x = s.countSegments(data)
        self.assertEqual(x, 6)

    def test_count_segments2(self):
        s = Solution()
        data = "                "
        x = s.countSegments(data)
        self.assertEqual(x, 0)


