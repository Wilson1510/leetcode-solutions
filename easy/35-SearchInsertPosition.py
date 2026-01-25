"""
Complexity:
- Time  : O(log n)
- Space : O(1)
"""
from typing import List


class Solution:
    # Runtime: 0ms
    # Memory Usage: 19.91MB
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        return low

    # Best time complexity solution (0ms)
    def searchInsertBestTime(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        return l

    # Best memory complexity solution (17.6MB)
    def searchInsertBestMemory(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l <= r:
            m = l + (r-l)//2
            if nums[m] >= target:
                r = m-1
            else:
                l = m+1
        return l    


if __name__ == "__main__":
    s = Solution()

    print(s.searchInsert([1,3,5,6], 5)) # 2
    print(s.searchInsert([1,3,5,6], 2)) # 1
    print(s.searchInsert([1,3,5,6], 7)) # 4
