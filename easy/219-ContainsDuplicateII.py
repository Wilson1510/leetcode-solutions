"""
Complexity:
- Time  : O(n)
- Space : O(n)
"""
from typing import List


class Solution:
    # Runtime: 32ms
    # Memory Usage: 36.6MB
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ref = {}
        for i, num in enumerate(nums):
            if num in ref and i - ref[num] <= k:
                return True
            ref[num] = i
        return False
            

    # Best time complexity solution (0ms)
    def containsNearbyDuplicateBestTime(self, nums: List[int], k: int) -> bool:
        window = set()

        for i, num in enumerate(nums):
            if num in window:
                return True
            window.add(num)
            if len(window) > k:
                window.remove(nums[i - k])

        return False

    # Best memory complexity solution (23.73MB)
    def containsNearbyDuplicateBestMemory(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            if i+k <= len(nums):
                tem = nums[i+1:i+k+1]
            else:
                tem = nums[i+1:len(nums)]

            if nums[i] in tem:
                return True
        
        return False 


if __name__ == "__main__":
    s = Solution()

    print(s.containsNearbyDuplicate([1,2,3,1], 3)) # True
    print(s.containsNearbyDuplicate([1,0,1,1], 1)) # True
    print(s.containsNearbyDuplicate([1,2,3,1,2,3], 2)) # False
