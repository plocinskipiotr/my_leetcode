class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        d = {}
        nums_size = len(nums)
        for i in range(nums_size):
            if nums[i] in d:
                return [i, d[nums[i]]]
            diff = target - nums[i]
            d |= {diff: i}
