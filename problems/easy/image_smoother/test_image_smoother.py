from unittest import TestCase
from image_smoother import Solution


class TestSolution(TestCase):
    def test_image_smoother(self):
        s = Solution()
        img = [[100, 200, 100], [200, 50, 200], [100, 200, 100]]
        x = s.imageSmoother(img)
        self.assertEqual([[137, 141, 137], [141, 138, 141], [137, 141, 137]], x)

    def test_image_smoother2(self):
        s = Solution()
        img = [[1,1,1],[1,0,1],[1,1,1]]
        x = s.imageSmoother(img)
        self.assertEqual([[0,0,0],[0,0,0],[0,0,0]], x)

    def test_image_smoother3(self):
        s = Solution()
        img = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
        x = s.imageSmoother(img)
        self.assertEqual([[0,0,0],[0,0,0],[0,0,0]], x)

