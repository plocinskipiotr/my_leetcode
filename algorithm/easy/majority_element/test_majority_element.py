from unittest import TestCase
from majority_element import Solution


class TestSolution(TestCase):
    def test_majority_element(self):
        s = Solution()
        data = [2, 2, 1, 1, 1, 2, 2]
        r = s.majorityElementVoting(data)
        self.assertEqual(2, r)
