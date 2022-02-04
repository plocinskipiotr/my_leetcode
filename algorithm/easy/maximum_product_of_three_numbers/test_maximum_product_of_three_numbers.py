from unittest import TestCase
from maximum_product_of_three_numbers import Solution


class TestSolution(TestCase):
    def test_maximum_product(self):
        s = Solution()
        nums = [1, 2, 3]
        x = s.maximumProduct(nums)
        self.assertEqual(x, 6)

    def test_maximum_product2(self):
        s = Solution()
        nums = [1, 2, 3, 4]
        x = s.maximumProduct(nums)
        self.assertEqual(x, 24)

    def test_maximum_product3(self):
        s = Solution()
        nums = [-1, -2, -3]
        x = s.maximumProduct(nums)
        self.assertEqual(x, -6)

    def test_maximum_product4(self):
        s = Solution()
        nums = [-100,-98,-1,2,3,4]
        x = s.maximumProduct(nums)
        self.assertEqual(x, 39200)
