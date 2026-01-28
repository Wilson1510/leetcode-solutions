"""
Complexity:
- Time  : O(n)
- Space : O(m) m = the number of unique char of s
"""
from collections import defaultdict


class Solution:
    # Runtime: 78ms
    # Memory Usage: 19.7MB
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        mapping = {}
        max_freq = 0
        max_length = 0

        for right in range(len(s)):
            mapping[s[right]] = mapping.get(s[right], 0) + 1
            max_freq = max(mapping[s[right]], max_freq)
            
            if right - left + 1 - max_freq > k:
                mapping[s[left]] -= 1
                left += 1

            max_length = max(right - left + 1, max_length)
        return max_length

    # Best time complexity solution (7ms)
    def characterReplacementBestTime(self, s: str, k: int) -> int:
        l = changes = max_freq = 0
        freq = defaultdict(int)
        for r in s:
            freq[r] += 1
            if freq[r] > max_freq: 
                max_freq = freq[r]
            elif changes == k:
                freq[s[l]] -= 1
                l += 1
            else:
                changes += 1
        
        return max_freq + changes

    # Best memory complexity solution (17.1MB)
    def characterReplacementBestMemory(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        
        left = 0
        result = 0
        frequencies = defaultdict(int)

        for right in range(len(s)):

            letter = s[right]
            frequencies[letter] +=1

            while (right-left+1) - max(frequencies.values()) > k:
                left_letter = s[left]
                frequencies[left_letter] -=1
                left +=1
            
            result = max(result, right-left+1)
        
        return result


if __name__ == "__main__":
    s = Solution()

    print(s.characterReplacement("ABAB", 2)) # 4
    print(s.characterReplacement("AABABBA", 1)) # 4
