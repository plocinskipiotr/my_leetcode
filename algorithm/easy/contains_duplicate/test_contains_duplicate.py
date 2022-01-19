from unittest import TestCase
from contains_duplicate import Solution

class TestSolution(TestCase):
    def test_contains_duplicate(self):
        s = Solution()
        t = s.containsDuplicate([1,1,1,3,3,4,3,2,4,2])
        self.assertTrue(t)

    def test_contains_duplicate2(self):
        s = Solution()
        t = s.containsDuplicate([1,2,3,4])
        self.assertFalse(t)

