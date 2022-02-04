from unittest import TestCase
from minimum_index_sum_of_two_lists import Solution


class TestSolution(TestCase):
    def test_find_restaurant(self):
        s = Solution()
        lst1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
        lst2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
        x = s.findRestaurant(lst1, lst2)
        self.assertEqual(['Shogun'], x)

    def test_find_restaurant2(self):
        s = Solution()
        lst1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
        lst2 = ["KFC", "Shogun", "Burger King"]
        x = s.findRestaurant(lst1, lst2)
        self.assertEqual(['Shogun'], x)

    def test_find_restaurant3(self):
        s = Solution()
        lst1 = ["Shogun", "KFC"]
        lst2 = ["KFC", "Shogun"]
        x = s.findRestaurant(lst1, lst2)
        self.assertEqual(['Shogun', 'KFC'], x)
