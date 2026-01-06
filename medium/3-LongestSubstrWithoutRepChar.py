"""
Complexity:
- Time  : O()
- Space : O()
"""
from collections import defaultdict


class Solution:
    # Runtime: 11ms
    # Memory Usage: 17.87MB
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start = 0
        max_len = 0

        for i, ch in enumerate(s):
            if ch in seen and seen[ch] >= start:
                start = seen[ch] + 1
            seen[ch] = i
            max_len = max(max_len, i - start + 1)

        return max_len
            

    # Best time complexity solution (2ms)
    def lengthOfLongestSubstringBestTime(self, s: str) -> int:
        a=0
        ss=""
        for i in s:
            if i not in ss:
                ss+=i
                a=max(a,len(ss))
            else:
                q=ss.index(i)
                ss=ss[q+1:]+i
                print(ss[q+1:]+i)
        return a

    # Best memory complexity solution (16.7MB)
    def lengthOfLongestSubstringBestMemory(self, s: str) -> int:
        ans = 0
        cnt = defaultdict(int)  # 窗口内的每种字母的出现次数
        left = 0  # 窗口左端点
        for i, ch in enumerate(s):
            cnt[ch] += 1
            while cnt[ch] > 1:
                cnt[s[left]] -= 1
                left += 1
            # while 循环结束后，现在 [left, i] 是一个合法的子串
            ans = max(ans, i - left + 1)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))
