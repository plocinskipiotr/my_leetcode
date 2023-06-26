from unittest import TestCase
from two_sum import Solution


class TestSolution(TestCase):
    def test_two_sum(self):
        s = Solution()

        data = [2, 7, 11, 15]
        target = 9
        x = s.twoSum(data, target)
        self.assertEqual(x, [0, 1])

        data = [3, 2, 4]
        target = 6
        x = s.twoSum(data, target)
        self.assertEqual(x, [1, 2])

    def test_reversed_hashmap_empty(self):
        s = Solution()
        data = []

        hashmap = s.reversed_hashmap(data)
        self.assertEqual(hashmap, {})

    def test_reversed_hashmap(self):
        s = Solution()
        data = [2, 7, 11, 15]

        hashmap = s.reversed_hashmap(data)
        self.assertEqual(hashmap, {2: 0, 7: 1, 11: 2, 15: 3})

        data = [3, 2, 4]

        hashmap = s.reversed_hashmap(data)
        self.assertEqual(hashmap, {3: 0, 2: 1, 4: 2})
