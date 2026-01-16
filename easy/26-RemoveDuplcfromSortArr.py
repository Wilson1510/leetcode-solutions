"""
Complexity:
- Time  : O(n)
- Space : O(1)
"""
from typing import List


class Solution:
    # Runtime: 3ms
    # Memory Usage: 20.62MB
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k

    # Best time complexity solution (0ms)
    def removeDuplicatesBestTime(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        slow, fast = 0,1
        pos = 1
        while fast < n:
            if nums[fast] == nums[slow]:
                fast += 1
            else:
                nums[pos] = nums[fast]
                slow += 1
                fast += 1
                pos += 1
                
        return pos

    # Best memory complexity solution (17.5MB)
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                l +=1
                nums[l] = nums[r]
        return l + 1


if __name__ == "__main__":
    s = Solution()
