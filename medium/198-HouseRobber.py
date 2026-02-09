"""
Complexity:
- Time  : O(n)
- Space : O(1)
"""
from typing import List


class Solution:
    # Runtime: 0ms
    # Memory Usage: 19.34MB
    def rob(self, nums: List[int]) -> int:
        prev2 = 0
        prev1 = 0

        for n in nums:
            curr = max(prev1, prev2 + n)
            prev2 = prev1
            prev1 = curr

        return prev1

    # Best time complexity solution (0ms)
    def robBestTime(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        if n == 1:
            return nums[0]
        if n == 2 :
            return max(nums[0],nums[1])
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,n):
            dp[i] = max(nums[i]+dp[i-2],dp[i-1])
        return dp[n-1]

    # Best memory complexity solution (16.6MB)
    def robBestMemory(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        dp2 = 0
        dp1 = nums[n - 1]
        dp = 0
        for i in range(n - 2, -1, -1):
            dp = max(nums[i] + dp2, dp1)
            dp2, dp1 = dp1, dp
        return dp


if __name__ == "__main__":
    s = Solution()

    print(s.rob([1, 2, 3, 1])) # 4
    print(s.rob([2, 7, 9, 3, 1])) # 12
    print(s.rob([2, 1, 1, 2])) # 4
