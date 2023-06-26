class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = self.reversed_hashmap(nums)

        for i in range(len(nums)):
            result = target - nums[i]
            if result in hashmap:
                if i != hashmap[result]:
                    return [i, hashmap[result]]

    def reversed_hashmap(self, nums: list[int]) -> dict:
        hashmap = dict()

        for item in range(len(nums)):
            hashmap[nums[item]] = item

        return hashmap
