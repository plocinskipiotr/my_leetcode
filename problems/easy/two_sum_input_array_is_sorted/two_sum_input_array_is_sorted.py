from typing import List


class Solution:
    def twoSum_binary_search(self, numbers: List[int], target: int) -> List[int]:
        n = 0

        while n < len(numbers) - 1:
            l = n
            r = len(numbers) - 1
            while r >= l:
                mid = (r + l) // 2

                if numbers[mid] + numbers[n] == target:
                    if mid != n:
                        return [n + 1, mid + 1]
                    else:
                        l = mid + 1
                elif numbers[mid] + numbers[n] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            n += 1
        return [-1, -1]

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            summa = numbers[l] + numbers[r]
            if summa == target:
                return [l + 1, r + 1]
            elif summa > target:
                r -= 1
            else:
                l += 1

        return [-1, -1]
