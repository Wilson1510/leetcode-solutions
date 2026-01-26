"""
Complexity:
- Time  : O(n.k log (k))
- Space : O(n.k)
"""
from typing import List
from collections import defaultdict


class Solution:
    # Runtime: 12ms
    # Memory Usage: 22MB
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ref = defaultdict(list)
        for word in strs:
            ref[''.join(sorted(word))].append(word)
        return list(ref.values())

    # Best time complexity solution (0ms)
    def groupAnagramsBestTime(self, strs:List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            key = ''.join(sorted(s))

            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        return list(groups.values())

    # Best memory complexity solution (18.3MB)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countMap = {}
        for i in s:
            if i in countMap:
                countMap[i] += 1
            else:
                countMap[i] = 1

        for i in t:
            if i in countMap and countMap[i]>0:
                countMap[i] -= 1
            else:
                return False
        
        return True

    def groupAnagramsBestMemory(self, strs: List[str]) -> List[List[str]]:
        ans = []
        isProcessed = [0]*len(strs)

        for i in range(len(strs)):
            if isProcessed[i] == 0:
                temp = [strs[i]]
                for j in range(i+1, len(strs)):
                    if self.isAnagram(strs[i], strs[j]):
                        temp.append(strs[j])
                        isProcessed[j] = 1
                ans.append(temp)

        return ans


if __name__ == "__main__":
    s = Solution()

    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])) # [["bat"],["nat","tan"],["ate","eat","tea"]]
    print(s.groupAnagrams([""])) # [[""]]
    print(s.groupAnagrams(["a"])) # [["a"]]
