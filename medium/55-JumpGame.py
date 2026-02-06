"""
Complexity:
- Time  : O(n)
- Space : O(1)
"""
from typing import List


class Solution:
    # Runtime: 23ms
    # Memory Usage: 20.25MB
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, jump in enumerate(nums):
            if i > max_reach:
                return False

            max_reach = max(max_reach, i + jump)

            if max_reach >= len(nums) - 1:
                return True
                
        return False

    # Best time complexity solution (34ms)
    def canJumpBestTime(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n-1

        for i in range(n-2,-1,-1):
            if nums[i] < goal - i:
                continue
            
            goal = i
        
        return not goal

    # Best memory complexity solution (17.8MB)
    def canJumpBestMemory(self, nums: List[int]) -> bool:
        jumpSet = set()
        jumpSet.add(len(nums) - 1)

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= min(jumpSet):
                jumpSet.add(i)

        return 0 in jumpSet


if __name__ == "__main__":
    s = Solution()

    print(s.canJump([2,3,1,1,4])) # True
    print(s.canJump([3,2,1,0,4])) # False
    print(s.canJump([2, 0])) # True
    print(s.canJump([2, 5, 0, 0])) # True
