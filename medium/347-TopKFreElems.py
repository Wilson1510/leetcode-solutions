"""
Complexity:
- Time  : O(n)
- Space : O(n)
"""
from typing import List
from collections import Counter


class Solution:
    # Runtime: 11ms
    # Memory Usage: 24.7MB
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for n, freq in count.items():
            bucket[freq].append(n)

        res = []
        
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res

    # Best time complexity solution (0ms)
    def topKFrequentBestTime(self, nums: List[int], k: int) -> List[int]:
        a=Counter(nums)
        return [num for num, _ in a.most_common(k)]

    # Best memory complexity solution (19.3MB)
    def topKFrequentBestMemory(self, nums: List[int], k: int) -> List[int]:
        s=set(nums)
        d=[]
        for i in s:
            d.append([nums.count(i),i])
        d.sort()
        return [d[-i][1] for i in range(1,k+1)]


if __name__ == "__main__":
    s = Solution()

    print(s.topKFrequent([1,1,1,2,2,3], 2)) # [1,2]
    print(s.topKFrequent([1], 1)) # [1]
    print(s.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2)) # [1, 2]
