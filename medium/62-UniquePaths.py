"""
Complexity:
- Time  : O(n^2)
- Space : O(n)
"""


class Solution:
    # Runtime: 0ms
    # Memory Usage: 19.27MB
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
    
        for _ in range(m-1):
            for j in range(n-2, -1, -1):
                dp[j] += dp[j+1]
        
        return dp[0]

    # Best time complexity solution (0ms)
    def uniquePathsBestTime(self, m: int, n: int) -> int:
        mem = [[1] * n for _ in range(m)]

        for curr_m in range(1, m):
            for curr_n in range(1, n):
                mem[curr_m][curr_n] = mem[curr_m - 1][curr_n] + mem[curr_m][curr_n - 1]
        
        return mem[m - 1][n - 1]

    # Best memory complexity solution (16.8MB)
    def uniquePathsBestMemory(self, m: int, n: int) -> int:
        paths = [[1 for _ in range(n)] for _ in range(m)]

        for r in range(m - 2, -1, -1):
            for c in range(n - 2, -1, -1):
                paths[r][c] = paths[r + 1][c] + paths[r][c + 1]

        return paths[0][0]


if __name__ == "__main__":
    s = Solution()

    print(s.uniquePaths(3, 7)) # 28
    print(s.uniquePaths(3, 2)) # 3
