"""
Complexity:
- Time  : O(mn)
- Space : O(n)
"""


class Solution:
    # Runtime: 205ms
    # Memory Usage: 19.5MB
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        t1, t2 = len(text1), len(text2)
        prev = [0] * (t2 + 1)
        
        for i in range(t1 - 1, -1, -1):
            curr = [0] * (t2 + 1)
            for j in range(t2 - 1, -1, -1):
                if text1[i] == text2[j]:
                    curr[j] = 1 + prev[j + 1]
                else:
                    curr[j] = max(prev[j], curr[j + 1])
            prev = curr
        return curr[0]


    # Best time complexity solution (27ms)
    def longestCommonSubsequenceBestTime(self, text1: str, text2: str) -> int:
        texts = set(text1) & set(text2)
        if len(texts) == 0:
            return 0
        t1 = [c for c in text1 if c in texts]
        t2 = [c for c in text2 if c in texts]
        dp = [0] * len(t2)
        for i in range(len(t1)):
            count = 0 
            for j in range(len(t2)):
                if dp[j] > count:
                    count = dp[j]
                elif t2[j] == t1[i]:
                    dp[j] = count + 1
        return max(dp)

    # Best memory complexity solution (18.69MB)
    def longestCommonSubsequenceBestMemory(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [0] * (m+1)
        for i in range(1, n+1):
            ndp = [0] * (m+1)
            c1 = text1[i-1]
            for j in range(1, m+1):
                c2 = text2[j-1]
                ndp[j] = max((1 if c1 == c2 else 0) + dp[j-1], ndp[j-1], dp[j])
            dp = ndp

        return dp[-1]


if __name__ == "__main__":
    s = Solution()

    print(s.longestCommonSubsequence("abcde", "ace" )) # 3
    print(s.longestCommonSubsequence("abc", "abc")) # 3
    print(s.longestCommonSubsequence("abc", "def")) # 0
    print(s.longestCommonSubsequence("abc", "bac")) # 2
    print(s.longestCommonSubsequence("abcde", "aecbd")) # 3
