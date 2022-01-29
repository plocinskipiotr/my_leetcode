from unittest import TestCase
from license_key_formatting import Solution


class TestSolution(TestCase):
    def test_license_key_formatting(self):
        s = Solution()
        data = '5F3Z-2e-9-w'
        k = 4
        x = s.licenseKeyFormatting(data, k)
        self.assertEqual('5F3Z-2E9W', x)

    def test_license_key_formatting2(self):
        s = Solution()
        data = '5F3Z-2ef-93-w1'
        k = 4
        x = s.licenseKeyFormatting(data, k)
        self.assertEqual('5F3-Z2EF-93W1', x)
