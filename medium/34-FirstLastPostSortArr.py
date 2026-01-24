"""
Complexity:
- Time  : O(log n)
- Space : O(1)
"""
from typing import List


class Solution:
    # Runtime: 0ms
    # Memory Usage: 20.76MB
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findBound(isFirst):
            low = 0
            high = len(nums) - 1

            ans = -1

            while low <= high:
                mid = (low + high) // 2
                if nums[mid] < target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    ans = mid
                    if isFirst:
                        high = mid - 1
                    else:
                        low = mid + 1
            return ans

        return [findBound(True), findBound(False)]

    # Best time complexity solution (0ms)
    def searchRangeBestTime(self, nums: List[int], target: int) -> List[int]:
        def find_first_last(is_first:bool)->int:
            low,high=0,len(nums)-1
            bound=-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    bound=mid
                    if is_first:
                        high=mid-1
                    else:
                        low=mid+1
                elif target>nums[mid]:
                    low=mid+1
                else:
                    high=mid-1
            return bound
        first=find_first_last(True)
        if first==-1:
            return [-1,-1]
        last=find_first_last(False)
        return [first,last]

    # Best memory complexity solution (18MB)
    def searchRangeBestTime(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        
        if target > nums[-1] or target < nums[0]:
            return [-1, -1]

        left  = 0
        right = len(nums)-1
        mid = (left + right) // 2
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                break
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if nums[mid] != target:
            return [-1, -1]
        else:
            left = mid
            right = mid
            for i in range(mid, -1, -1):
                if nums[i]!=target:
                    left = i+1
                    break
                else:
                    left = i


            for i in range(mid, len(nums)):
                if nums[i] != target:
                    right = i-1
                    break
                else:
                    right = i
            return [left, right]


if __name__ == "__main__":
    s = Solution()

    print(s.searchRange([5,7,7,8,8,10], 8)) # [3, 4]
    print(s.searchRange([5,7,7,8,8,10], 6)) # [-1, -1]
    print(s.searchRange([], 0)) # [-1, -1]
