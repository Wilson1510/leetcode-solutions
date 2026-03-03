"""
Complexity:
- Time  : O(n)
- Space : O(n)
"""
from typing import List


class Solution:
    # Runtime: 4ms
    # Memory Usage: 20MB
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = 1 + ans[i & (i - 1)]
        return ans

    # Best time complexity solution (0ms)
    def countBitsBestTime(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(n + 1):
            ans[i] = i.bit_count()
        return ans

    # Best memory complexity solution (17.4MB)
    def countBitsBestMemory(self, n: int) -> List[int]:
        # DP
        # dp[i] = 1 plus dp[(i << 1) >> 1]

        # if n == 0: return [0]
        # if n == 1: return [0, 1]

        # base case:
        dp = [0 for _ in range(n + 1)]
        for i in range(n + 1):
            # check if rightmost bit is a 1
            dp[i] = dp[i >> 1] + (i & 1)

        return dp


if __name__ == "__main__":
    s = Solution()

    print(s.countBits(2))  # [0, 1, 1]
    print(s.countBits(50))  # [0, 1, 1, 2, 1, 2]
