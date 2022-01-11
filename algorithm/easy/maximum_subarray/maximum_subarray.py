class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr_sum = max_sum = nums[0]

        for el in nums[1:]:
            curr_sum = max(el, curr_sum + el)
            max_sum = max(max_sum, curr_sum)

        return max_sum
