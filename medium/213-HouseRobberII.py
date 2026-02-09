"""
Complexity:
- Time  : O(n)
- Space : O(1)
"""
from typing import List


class Solution:
    # Runtime: 0ms
    # Memory Usage: 19.3MB
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # Kasus khusus jika hanya ada satu rumah
        if n == 1:
            return nums[0]

        # Fungsi helper untuk House Robber I (Linear)
        def linear_rob(houses):
            prev2, prev1 = 0, 0
            for amount in houses:
                curr = max(prev1, prev2 + amount)
                prev2 = prev1
                prev1 = curr
            return prev1

        # Bandingkan dua skenario
        return max(linear_rob(nums[:-1]), linear_rob(nums[1:]))

    # Best time complexity solution (0ms)
    def robBestTime(self, nums: List[int]) -> int:
        n=len(nums)
        def robbing(nums: List[int]) -> int:
            dp=[0]*len(nums)
            if len(nums)<3: return max(nums)
            dp[0]=nums[0]
            dp[1]=max(nums[0],nums[1])
            for i in range(2,len(nums)):
                dp[i]=max(nums[i]+dp[i-2], dp[i-1])
            return dp[-1]
        if len(nums)<4: return max(nums)
        else:
            # print(nums[1:])
            return max(robbing(nums[:n-1]),robbing(nums[1:]))

    # Best memory complexity solution (16.8MB)
    def robBestMemory(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def helper(nums) -> int:
            p = [0,0]
            for n in nums:
                p[0], p[1] = p[1], max(p[1], n+p[0])
            return p[1]
        return max(helper(nums[:-1]), helper(nums[1:]))     


if __name__ == "__main__":
    s = Solution()

    print(s.rob([2, 3, 2])) # 3
    print(s.rob([1, 2, 3, 1])) # 4
    print(s.rob([1, 2, 3])) # 3
