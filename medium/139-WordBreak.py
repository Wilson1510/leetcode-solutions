"""
Complexity:
- Time  : O(n*m*k) n = len(s), m = len(wordDict), k = len(word) in wordDict
- Space : O(n)
"""
from typing import List


class Solution:
    # Runtime: 0ms
    # Memory Usage: 19.38MB
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1, -1):
            for word in wordDict:
                if s.startswith(word, i) and dp[i + len(word)]:
                    dp[i] = True
                    break
        return dp[0]
                

    # Best time complexity solution (0ms)
    def wordBreakBestTime(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1) # does the string starting at index i break
        dp[len(s)] = True # empty string is breakable

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i+len(word)] == word and dp[i + len(word)]:
                    dp[i] = True
                    break
        
        return dp[0]

    # Best memory complexity solution (17MB)
    def wordBreakBestMemory(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        can_split: list[bool] = [False] * (len(s) + 1)
        can_split[0] = True

        for right in range(1, len(s) + 1):
            for left in range(right):
                if can_split[left] and s[left:right] in word_set:
                    can_split[right] = True
                    break

        return can_split[len(s)]


if __name__ == "__main__":
    s = Solution()

    print(s.wordBreak("leetcode", ["leet","code"])) # True
    print(s.wordBreak("applepenapple", ["apple","pen"])) # True
    print(s.wordBreak("catsandog", ["cats","dog","sand","and","cat"])) # False
    print(s.wordBreak("cars", ["car","ca","rs"])) # True
    print(s.wordBreak("a", ["a"])) # True
    print(s.wordBreak("a"*150 + "b", ["a" * i for i in range(1, 11)])) # False