class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        for i in range(len(nums)):
            try:
                while nums[i] == nums[i + 1]:
                    nums.pop(i + 1)
            except IndexError:
                break

        return len(nums)

    def removeDuplicates2(self, nums: list[int]) -> int:

        if not nums:
            return 0

        prev = nums[0]
        i = 1
        while i in range(len(nums)):
            curr = nums[i]
            if curr == prev:
                nums.pop(i)
            else:
                prev = curr
                i += 1

        return len(nums)

    def removeDuplicates3(self, nums: list[int]) -> int:

        if len(nums) == 0:
            return 0
        i = 1

        for j in range(len(nums) - 1):
            if nums[j] != nums[j + 1]:
                nums[i] = nums[j + 1]
                i += 1

        return i
