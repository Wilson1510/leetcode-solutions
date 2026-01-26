"""
Complexity:
- Time  : O(n)
- Space : O(n)
"""
from typing import List


class Solution:
    # Runtime: 7ms
    # Memory Usage: 31.44MB
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

    # Best time complexity solution (0ms)
    def containsDuplicateBestTime(self, nums: List[int]) -> bool:
        seen = set(nums)
        return len(seen) != len(nums)

    # Best memory complexity solution (25.86MB)
    def containsDuplicateBestMemory(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False


if __name__ == "__main__":
    s = Solution()

    print(s.containsDuplicate([1,2,3,1])) # True
    print(s.containsDuplicate([1,2,3,4])) # False
    print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2])) # True
