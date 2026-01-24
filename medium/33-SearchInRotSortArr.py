"""
Complexity:
- Time  : O(log n)
- Space : O(1)
"""
from typing import List


class Solution:
    # Runtime: 0ms
    # Memory Usage: 19.62MB
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
                    
        return -1

    # Best time complexity solution (0ms)
    def searchBestTime(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r)//2

            if nums[mid] == target:
                return mid
            # if right sorted     
            if nums[mid] < nums[r]:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
               
            else:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
                    
        return -1

    # Best memory complexity solution (17.1MB)
    def searchBestMemory(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            # 左半段有序
            if nums[l] <= nums[mid]:
                # target 落在 [nums[l], nums[mid]) 这个有序区间
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # 右半段有序
            else:
                # target 落在 (nums[mid], nums[r]] 这个有序区间
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1


if __name__ == "__main__":
    s = Solution()

    print(s.search([4,5,6,7,0,1,2], 0)) # 4
    print(s.search([4,5,6,7,0,1,2], 3)) # -1
    print(s.search([1], 0)) # -1
    print(s.search([1, 3], 3)) # 1