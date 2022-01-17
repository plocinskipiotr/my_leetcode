from unittest import TestCase
from best_time_to_buy_and_sell_stock import Solution


class TestSolution(TestCase):
    def test_max_profit(self):
        s = Solution()
        data = [7, 1, 5, 3, 6, 4]
        x = s.maxProfit(data)
        self.assertEqual(x, 5)

    def test_max_profit_0(self):
        s = Solution()
        data = [7,6,4,3,1]
        x = s.maxProfit(data)
        self.assertEqual(x, 0)
