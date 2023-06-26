from unittest import TestCase
from range_sum_query_immutable import NumArray


class TestNumArray(TestCase):
    def test_sum_range(self):
        t = NumArray([-2, 0, 3, -5, 2, -1])

        s = t.sumRange(0, 2)
        self.assertEqual(s, 1)
        s = t.sumRange(0, 5)
        self.assertEqual(s, -3)

        t = NumArray([1])
        s = t.sumRange(0, 0)
        self.assertEqual(s, 1)
