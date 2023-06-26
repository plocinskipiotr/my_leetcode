from unittest import TestCase
from teemo_attacking import Solution


class TestSolution(TestCase):
    def test_find_poisoned_duration(self):
        s = Solution()
        timeSeries = [1, 4]
        duration = 2

        x = s.findPoisonedDuration(timeSeries, duration)
        self.assertEqual(4, x)

    def test_find_poisoned_duration2(self):
        s = Solution()
        timeSeries = [1, 2]
        duration = 2

        x = s.findPoisonedDuration(timeSeries, duration)
        self.assertEqual(3, x)
