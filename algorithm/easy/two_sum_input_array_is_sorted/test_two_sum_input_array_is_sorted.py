from unittest import TestCase
from two_sum_input_array_is_sorted import Solution


class TestSolution(TestCase):
    def test_two_sum_0(self):
        s = Solution()
        numbers, target = [2, 7, 11, 15], 9
        x = s.twoSum(numbers, target)
        self.assertEqual([1, 2], x)

    def test_two_sum_1(self):
        s = Solution()
        numbers, target = [2, 3, 4], 6
        x = s.twoSum(numbers, target)
        self.assertEqual([1, 3], x)

    def test_two_sum_2(self):
        s = Solution()
        numbers, target = [-1, 0], -1
        x = s.twoSum(numbers, target)
        self.assertEqual([1, 2], x)

    def test_two_sum_3(self):
        s = Solution()
        numbers, target = [1, 3, 4, 4], 8
        x = s.twoSum(numbers, target)
        self.assertEqual([3, 4], x)
