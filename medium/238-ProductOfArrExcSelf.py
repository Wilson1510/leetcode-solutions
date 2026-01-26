"""
Complexity:
- Time  : O(n)
- Space : O(1)
"""
from typing import List


class Solution:
    # Runtime: 27ms
    # Memory Usage: 25.6MB
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        right_product = 1
        for i in range(n - 1, -1, -1):
            res[i] = res[i] * right_product
            right_product = right_product * nums[i]

        return res

    # Best time complexity solution (3ms)
    def productExceptSelfBestTime(self, nums: List[int]) -> List[int]:
        prod = 1
        for n in nums: prod *= n
        if prod: return [prod // i for i in nums]

        prod = 1
        zeros = 0
        for n in nums:
            if n: prod *= n
            else: zeros += 1

        if zeros > 1: prod = 0
        return [0 if i else prod for i in nums]

    # Best memory complexity solution (21.3MB)
    def productExceptSelfBestMemory(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = [0] * 62
        lookup = [0] * 62

        for num in nums:
            freq[num + 30] += 1

        for k in range(62):
            p = 1

            if freq[k] == 0:
                continue

            for v in range(62):
                if freq[v] == 0:
                    continue

                if v == k:
                    if freq[v] > 1:
                        p *= (v - 30) ** (freq[v] - 1)
                else:
                    p *= (v - 30) ** freq[v]

            lookup[k] = p

        for i in range(n):
            nums[i] = lookup[nums[i] + 30]

        return nums


if __name__ == "__main__":
    s = Solution()

    print(s.productExceptSelf([1,2,3,4])) # [24,12,8,6]
    print(s.productExceptSelf([-1,1,0,-3,3])) # [0,0,9,0,0]
