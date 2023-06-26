from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.accum = [0]
        for i in range(len(nums)):
            cur = self.accum[-1] + nums[i]
            self.accum.append(cur)

    def sumRange(self, left: int, right: int) -> int:
        res = self.accum[right + 1] - self.accum[left]
        return res

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
