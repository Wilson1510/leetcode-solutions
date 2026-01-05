"""
Complexity:
- Time  : O(m*n)
- Space : O(m*n)
"""

class Solution:
    # Runtime: 3ms
    # Memory Usage: 17.53MB
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if j == len(p):
                memo[(i, j)] = i == len(s)
            
            else:
                match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
                if (j + 1) < len(p) and p[j + 1] == '*':
                    memo[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
                
                elif match:
                    memo[(i, j)] = dfs(i + 1, j + 1)
                
                else:
                    memo[(i, j)] = False

            return memo[(i, j)]
        
        return dfs(0, 0)
            

    # Best time complexity solution (55ms)
    def isMatchBestTime(self, s: str, p: str) -> bool:
        i, j = len(s) - 1, len(p) - 1
        return self.backtrack({}, s, p, i, j)

    def backtrack(self, cache, s, p, i, j):
        key = (i, j)
        if key in cache:
            return cache[key]

        if i == -1 and j == -1:
            cache[key] = True
            return True

        if i != -1 and j == -1:
            cache[key] = False
            return cache[key]

        if i == -1 and p[j] == '*':
            k = j
            while k != -1 and p[k] == '*':
                k -= 2
            
            if k == -1:
                cache[key] = True
                return cache[key]
            
            cache[key] = False
            return cache[key]
        
        if i == -1 and p[j] != '*':
            cache[key] = False
            return cache[key]

        if p[j] == '*':
            if self.backtrack(cache, s, p, i, j - 2):
                cache[key] = True
                return cache[key]
            
            if p[j - 1] == s[i] or p[j - 1] == '.':
                if self.backtrack(cache, s, p, i - 1, j):
                    cache[key] = True
                    return cache[key]
        
        if p[j] == '.' or s[i] == p[j]:
            if self.backtrack(cache, s, p, i - 1, j - 1):
                cache[key] = True
                return cache[key]

        cache[key] = False
        return cache[key] 

    # Best memory complexity solution (16.7MB)
    def isMatchBestMemory(self, s: str, p: str) -> bool:
        if not p:
            return not s
        first_match = bool(s) and (p[0] == s[0] or p[0] == '.')
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])


if __name__ == "__main__":
    s = Solution()
    print(s.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*c"))
    print(s.isMatch("aa", "a"))  # False
    print(s.isMatch("aa", "a*"))  # True
    print(s.isMatch("ab", ".*"))  # True
    print(s.isMatch("adceb", "*a*b"))  # False

