"""
Complexity:
- Time  : O(n^2)
- Space : O(1)
"""


class Solution:
    # Runtime: 119ms
    # Memory Usage: 19.36MB
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            for j in range(2):
                left = i
                right = i + j

                while left >= 0 and right < len(s) and s[left] == s[right]:
                    count += 1
                    left -= 1
                    right += 1
        return count

    # Best time complexity solution (5ms)
    def countSubstringsBestTime(self, s: str) -> int:
        n = len(s)
        count = n
        for p in range(n):
            p_left = p-1
            p_right = p+1
            if p_left >= 0 and s[p_left] == s[p]:
                continue
            while p_right <= n-1 and s[p_right] == s[p]:
                p_right += 1
            shift = p_right - p
            shift_count = int((shift) * (shift - 1) / 2)
            count += shift_count
            while p_left >= 0 and p_right <= n-1:
                if s[p_left] == s[p_right]:
                    count += 1
                    p_left -= 1
                    p_right += 1
                else:
                    break
        return count

    # Best memory complexity solution (17.21MB)
    def countSubstringsBestMemory(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        return count


if __name__ == "__main__":
    s = Solution()

    print(s.countSubstrings("abc")) # 3
    print(s.countSubstrings("aaa")) # 6
    print(s.countSubstrings("a"*1000)) # 500500
    print(s.countSubstrings("ababab" * 200)) # 360600
    print(s.countSubstrings("a" * 500 + "b" + "a" * 500)) # 251001
    print(s.countSubstrings("abc" * 666)) # 1998
    print(s.countSubstrings("x" * 100 + "racecar".join(["a"*200, "a"*200]) + "y" * 100)) # 50512
