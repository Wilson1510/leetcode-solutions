"""
Complexity:
- Time  : O(n * m)
- Space : O(1)
"""

class Solution:
    # Runtime: 0ms
    # Memory Usage: 19.46MB
    def strStr(self, haystack: str, needle: str) -> int:
        n, h = len(needle), len(haystack)
    
        if n > h:
            return -1
        
        for i in range(h - n + 1):
            if haystack[i:i+n] == needle:
                return i
                
        return -1

    # Best time complexity solution (0ms)
    def strStrBestTime(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        
        len_h = len(haystack)
        len_n = len(needle)
        
        for i in range(len_h - len_n + 1):
            
            if haystack[i] != needle[0]:
                continue 
            
            if haystack[i : i + len_n] == needle:
                return i
                
        return -1

    # Best memory complexity solution (16.6MB)
    def strStrBestMemory(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            s,tmp = 0,i
            while s< len(needle) and tmp < len(haystack) and needle[s] == haystack[tmp]:
                
                s+=1
                tmp +=1
            if s == len(needle):
                return i
        return -1


if __name__ == "__main__":
    s = Solution()

    print(s.strStr("sadbutsad", "sad"))
    print(s.strStr("leetcode", "leeto"))
