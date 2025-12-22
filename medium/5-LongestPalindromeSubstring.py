"""
Complexity:
- Time  : O(n²)
- Space : O(1)
"""

class Solution:
    # Runtime: 265 ms
    # Memory Usage: 17.23 MB
    def longestPalindrome(self, s: str) -> str:
        length = len(s)

        start, max_length = 0, 1

        for i in range(length):
            for j in range(2):
                left = i
                right = i + j

                while left >= 0 and right < length and s[left] == s[right]:
                    if right - left + 1 > max_length:
                        start = left
                        max_length = right - left + 1
                    left -= 1
                    right += 1

        return s[start:start+max_length]

    # Best time complexity solution (52 ms)
    def longestPalindromeBestTime(self, s: str) -> str:
        res=""
        reslen=0

        for i in range(len(s)):
            # even len
            l=r=i
            while 0<=l and r<len(s) and s[l]==s[r]:
                if (r-l+1) > reslen:
                    res=s[l:r+1]
                    reslen=(r-l+1)

                l-=1
                r+=1
            
            # odd len
            l,r=i,i+1
            while 0<=l and r<len(s) and s[l]==s[r]:
                if (r-l+1) > reslen:
                    res=s[l:r+1]
                    reslen=(r-l+1)

                l-=1
                r+=1

        return res

    # Best memory complexity solution (16.858 MB)
    def longestPalindromeBestMemory(self, s: str) -> str:
        res=""
        reslen=0

        for i in range(len(s)):
            # even len
            l=r=i
            while 0<=l and r<len(s) and s[l]==s[r]:
                if (r-l+1) > reslen:
                    res=s[l:r+1]
                    reslen=(r-l+1)

                l-=1
                r+=1
            
            # odd len
            l,r=i,i+1
            while 0<=l and r<len(s) and s[l]==s[r]:
                if (r-l+1) > reslen:
                    res=s[l:r+1]
                    reslen=(r-l+1)

                l-=1
                r+=1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("cbbd"))