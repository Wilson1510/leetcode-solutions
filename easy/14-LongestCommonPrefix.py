"""
Complexity:
- Time  : O(n*m)
- Space : O(1)
"""
from typing import List


class Solution:
    # Runtime: 0ms
    # Memory Usage: 19.41MB
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        for i in range(len(strs[0])):
            c = strs[0][i]
            for s in strs[1:]:
                if i >= len(s) or s[i] != c:
                    return strs[0][:i]
        return strs[0]
            

    # Best time complexity solution (0ms)
    def longestCommonPrefixBestTime(self, v: List[str]) -> str:
        ans=""
        v=sorted(v)
        first=v[0]
        last=v[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 


    # Best memory complexity solution (16.8MB)
    def longestCommonPrefixBestMemory(self, strs: List[str]) -> str:
        first = strs[0]
        for i in range(len(first)):
            c = first[i]

            for j in range(1, len(strs)):
                cur_str = strs[j]
                if i >= len(cur_str) or c != cur_str[i]:
                    return first[:i]

        return first


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))
    print(s.longestCommonPrefix(["dog","racecar","car"]))
    print(s.longestCommonPrefix(["a"]))
    print(s.longestCommonPrefix([]))
    print(s.longestCommonPrefix(["aa","a"]))
