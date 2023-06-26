from unittest import TestCase
from remove_element import Solution


class TestSolution(TestCase):
    def test_remove_element(self):
        s = Solution()
        val = 2
        data = [1, 2, 2, 3, 4, 5]

        x = s.removeElement(data, val)

        self.assertEqual(4, x)

        val = 2
        data = [1,1,1,1,1,2]

        x = s.removeElement(data, val)

        self.assertEqual(5, x)

        val = 2
        data = [9,9,9,2,1,1,1,3,4]

        x = s.removeElement(data, val)

        self.assertEqual(8, x)


