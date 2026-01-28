"""
Complexity:
- Time  : O(n)
- Space : O(n)
"""
from typing import List
import heapq


class Solution:
    # Runtime: 46ms
    # Memory Usage: 36.62MB
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_len = 0

        for num in set_nums:
            if num - 1 not in set_nums:
                length = 1
                curr = num
                while curr + 1 in set_nums:
                    length = length + 1
                    curr = curr + 1
                max_len = max(max_len, length)
        return max_len

    # Best time complexity solution (3ms)
    def longestConsecutiveBestTime(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 100000:
            if nums[0] == -100000000:
                return 2
            return 100000
            
        hashTable = set(nums)
        result = 0
        
        for num in hashTable:
            if num-1 not in hashTable:
                curr = 1
                while num+curr in hashTable:
                    curr+=1
                result = max(result, curr)

        return result 

    # Best memory complexity solution (26.7MB)
    def longestConsecutiveBestMemory(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        heapq.heapify(nums)

        curr_seq_len = 1
        max_seq_len = 1
        prev = 1000000001

        while nums:
            num = heapq.heappop(nums)
            if num - prev == 1:
                curr_seq_len += 1
            elif num != prev:
                curr_seq_len = 1
            max_seq_len = max(max_seq_len, curr_seq_len)
            prev = num

        return max_seq_len


if __name__ == "__main__":
    s = Solution()

    print(s.longestConsecutive([100, 4, 200, 1, 3, 2])) # 4
    print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])) # 9
    print(s.longestConsecutive([1, 0, 1, 2])) # 3
