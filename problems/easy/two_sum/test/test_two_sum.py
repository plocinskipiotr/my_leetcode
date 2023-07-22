from problems.easy.two_sum.src.two_sum import Solution


class TestSolution:
    def test_000(self):
        s = Solution()

        nums = [2, 7, 11, 15]
        target = 9
        assert s.twoSum(nums, target) == [1, 0]

    def test_001(self):
        s = Solution()

        nums = [3, 2, 4]
        target = 6
        assert s.twoSum(nums, target) == [2, 1]

    def test_002(self):
        s = Solution()

        nums = [3, 3]
        target = 6
        assert s.twoSum(nums, target) == [1, 0]

    def test_003(self):
        s = Solution()

        nums = [2, 7, 11, 15, 6, 3]
        target = 8
        assert s.twoSum(nums, target) == [4, 0]
