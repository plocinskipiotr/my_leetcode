from unittest import TestCase
from contains_duplicate_2 import Solution


class TestSolution(TestCase):
    def test_contains_nearby_duplicate(self):
        s = Solution()
        nums = [1, 2, 3, 1]
        k = 3

        t = s.containsNearbyDuplicateSet(nums, k)
        self.assertTrue(t)

    def test_contains_nearby_duplicate2(self):
        s = Solution()
        nums = [1, 2, 3, 1, 2, 3]
        k = 2

        t = s.containsNearbyDuplicateSet(nums, k)
        self.assertFalse(t)

    def test_contains_nearby_duplicate3(self):
        s = Solution()
        nums = [1, 0, 1, 1]
        k = 1

        t = s.containsNearbyDuplicateSet(nums, k)
        self.assertTrue(t)

    def test_contains_nearby_duplicate4(self):
        s = Solution()
        nums = [1, 2, 1]
        k = 0

        t = s.containsNearbyDuplicateSet(nums, k)
        self.assertFalse(t)

    def test_contains_nearby_duplicate5(self):
        s = Solution()
        nums = [1, 2, 1]
        k = 0

        t = s.containsNearbyDuplicateSet(nums, k)
        self.assertFalse(t)

    def test_contains_nearby_duplicate6(self):
        s = Solution()
        nums = [1, 2, 7, 4, 5, 3, 2]
        k = 4

        t = s.containsNearbyDuplicateSet(nums, k)
        self.assertFalse(t)

    def test_contains_nearby_duplicate7(self):
        s = Solution()
        nums = [1, 2, 3, 4, 2]
        k = 7

        t = s.containsNearbyDuplicateSet(nums, k)
        self.assertTrue(t)

    def test_contains_nearby_duplicate8(self):
        s = Solution()
        nums = [1, 2, 3, 4, 5]
        k = 7

        t = s.containsNearbyDuplicateSet(nums, k)
        self.assertFalse(t)

    def test_contains_nearby_duplicate9(self):
        s = Solution()
        nums = []
        k = 1

        t = s.containsNearbyDuplicateSet(nums, k)
        self.assertFalse(t)

