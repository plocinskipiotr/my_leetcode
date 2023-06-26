from unittest import TestCase
from can_place_flowers import Solution


class TestSolution(TestCase):
    def test_can_place_flowers(self):
        s = Solution()
        flowerbed = [1, 0, 0, 0, 1]
        r = s.canPlaceFlowers(flowerbed, 1)
        self.assertTrue(r)

    def test_can_place_flowers2(self):
        s = Solution()
        flowerbed = [0, 0, 0, 0, 0]
        r = s.canPlaceFlowers(flowerbed, 3)
        self.assertTrue(r)

    def test_can_place_flowers3(self):
        s = Solution()
        flowerbed = [0]
        r = s.canPlaceFlowers(flowerbed, 1)
        self.assertTrue(r)

    def test_can_place_flowers4(self):
        s = Solution()
        flowerbed = [1]
        r = s.canPlaceFlowers(flowerbed, 0)
        self.assertTrue(r)

    def test_can_place_flowers5(self):
        s = Solution()
        flowerbed = [0, 0]
        r = s.canPlaceFlowers(flowerbed, 1)
        self.assertTrue(r)

    def test_can_place_flowers6(self):
        s = Solution()
        flowerbed = [1, 0]
        r = s.canPlaceFlowers(flowerbed, 0)
        self.assertTrue(r)

    def test_can_place_flowers7(self):
        s = Solution()
        flowerbed = [0, 1]
        r = s.canPlaceFlowers(flowerbed, 0)
        self.assertTrue(r)

    def test_can_place_flowers8(self):
        s = Solution()
        flowerbed = [1, 1]
        r = s.canPlaceFlowers(flowerbed, 0)
        self.assertTrue(r)

    def test_can_place_flowers81(self):
        s = Solution()
        flowerbed = [0, 0, 0]
        r = s.canPlaceFlowers(flowerbed, 2)
        self.assertTrue(r)

    def test_can_place_flowers9(self):
        s = Solution()
        flowerbed = [1, 0, 1]
        r = s.canPlaceFlowers(flowerbed, 0)
        self.assertTrue(r)

    def test_can_place_flowers10(self):
        s = Solution()
        flowerbed = [1, 0, 0]
        r = s.canPlaceFlowers(flowerbed, 1)
        self.assertTrue(r)

    def test_can_place_flowers11(self):
        s = Solution()
        flowerbed = [0, 0, 1]
        r = s.canPlaceFlowers(flowerbed, 1)
        self.assertTrue(r)

    def test_can_place_flowers12(self):
        s = Solution()
        flowerbed = [1, 0, 0, 0, 0, 0, 1]
        r = s.canPlaceFlowers(flowerbed, 2)
        self.assertTrue(r)

    def test_can_place_flowers13(self):
        s = Solution()
        flowerbed = [0, 1, 0, 0, 0, 0, 1]
        r = s.canPlaceFlowers(flowerbed, 1)
        self.assertTrue(r)

    def test_can_place_flowers14(self):
        s = Solution()
        flowerbed = [1, 0, 0, 0, 0, 1, 0]
        r = s.canPlaceFlowers(flowerbed, 1)
        self.assertTrue(r)

    def test_can_place_flowers15(self):
        s = Solution()
        flowerbed = [0, 1, 0, 0, 0, 1, 0]
        r = s.canPlaceFlowers(flowerbed, 1)
        self.assertTrue(r)

    def test_can_place_flowers16(self):
        s = Solution()
        flowerbed = [0,0,1,0,0]
        r = s.canPlaceFlowers(flowerbed, 1)
        self.assertTrue(r)
