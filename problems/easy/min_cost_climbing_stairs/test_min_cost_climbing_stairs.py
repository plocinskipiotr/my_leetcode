from unittest import TestCase
from min_cost_climbing_stairs import Solution


class TestSolution(TestCase):
    def test_min_cost_climbing_stairs_0(self):
        s = Solution()
        cost = [10, 15, 20]
        result = s.minCostClimbingStairs(cost)
        self.assertEqual(15, result)

    def test_min_cost_climbing_stairs_1(self):
        s = Solution()
        cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        result = s.minCostClimbingStairs(cost)
        self.assertEqual(6, result)
