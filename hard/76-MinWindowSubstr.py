"""
Complexity:
- Time  : O(n)
- Space : O(m) m is the number of unique char of t
"""
from collections import defaultdict, Counter


class Solution:
    # Runtime: 63ms
    # Memory Usage: 19.86MB
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""

        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        count_s = {}
        have, need = 0, len(count_t)
        res, res_len = [-1, -1], float("inf")
        left = 0

        for right in range(len(s)):
            char = s[right]
            count_s[char] = count_s.get(char, 0) + 1
            
            if char in count_t and count_s[char] == count_t[char]:
                have += 1

            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = (right - left + 1)

                char_left = s[left]
                count_s[char_left] -= 1
                if char_left in count_t and count_s[char_left] < count_t[char_left]:
                    have -= 1
                left += 1
                
        l, r = res
        return s[l : r + 1] if res_len != float("inf") else ""

    # Best time complexity solution (13ms)
    def minWindowBestTime(self, s: str, t: str) -> str:
        m=len(s)
        n=len(t)
        if t in s:
            return t
        if m<n:
            return ""
        for i in set(t):
            if i not in s:
                return ""
        char_cnt=defaultdict(int)
        for ch in t:
            char_cnt[ch]+=1
        
        left=0
        target=n
        min_interval=(0,float("inf"))
        for ind, ch in enumerate(s):
            if char_cnt[ch]>0:
                target-=1
            char_cnt[ch]-=1
            if target==0:
                ch_left=s[left]
                while char_cnt[ch_left]!=0:
                    char_cnt[ch_left]+=1
                    left+=1
                    ch_left=s[left]
                if ind-left<min_interval[1]-min_interval[0]:
                    min_interval=(left, ind)
                char_cnt[ch_left]+=1
                left+=1
                target+=1
        print(min_interval[0])
        print(min_interval[1]+1)   
        return "" if min_interval[1]>m-1 else s[min_interval[0]:min_interval[1]+1]

    # Best memory complexity solution (17.1MB)
    def minWindowBestMemory(self, s: str, t: str) -> str:
        if len(t) > len(s) or not set(t) <= set(s):
            return ""

        goal = Counter(t)

        res = ""
        curr = Counter()
        right = 0
        for left in range(len(s)):
            # eat until the goal is reached or the string is exhausted
            while right < len(s) and not curr >= goal:
                curr[s[right]] += 1
                right += 1

            # check goal is reached
            if curr >= goal:
                if not res or right - left < len(res):
                    res = s[left:right]

            # # if the string is 
            # if right == len(s):
            #     break

            # prepare for the next iteration by discarding the current left
            curr[s[left]] -= 1

        return res


if __name__ == "__main__":
    s = Solution()

    print(s.minWindow("ADOBECODEBANC", "ABC")) # "BANC"
    print(s.minWindow("a", "a")) # "a"
    print(s.minWindow("a", "aa")) # ""
