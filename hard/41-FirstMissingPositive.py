"""
Complexity:
- Time  : O(n)
- Space : O(1)
"""
from typing import List
import heapq


class Solution:
    # Runtime: 55ms
    # Memory Usage: 30.9MB
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
    
        for i in range(n):
            # Selama angka berada di rentang [1, n] 
            # dan belum berada di posisi yang benar (indeks nums[i]-1)
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Tukar angka ke posisi "rumahnya"
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

        # Cek rak buku dari depan
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        return n + 1
            

    # Best time complexity solution (4ms)
    def firstMissingPositiveBestTime(self, nums: List[int]) -> int:
        nums = set(nums)
        
        n = len(nums)
        if 1 not in nums: return 1

        nums = sorted(nums)
        lo = bi = nums.index(1)
        mid = 0
        hi = len(nums)
        if hi -bi == nums[-1]:
            return nums[-1]+1
        
        while lo < hi:
            mid = (lo + hi) // 2
            if mid - bi+1 == nums[mid]:
                lo = mid+1
            else:
                hi = mid
        return lo -bi+1

    # Best memory complexity solution (25MB)
    def firstMissingPositiveBestMemory(self, nums: List[int]) -> int:
        cur_smallest = 1

        heapq.heapify(nums)
        num = heapq.heappop(nums)

        while nums and num <= 0:
            num = heapq.heappop(nums)

        if num > 0:
            if cur_smallest < num:
                return cur_smallest
            else:
                cur_smallest = 1 + num
            
        while nums:
            num = heapq.heappop(nums)
            if cur_smallest < num:
                return cur_smallest
            cur_smallest = 1 + num

        return cur_smallest


if __name__ == "__main__":
    s = Solution()

    print(s.firstMissingPositive([1, 2, 0])) # 3
    print(s.firstMissingPositive([3,4,-1,1])) # 2
    print(s.firstMissingPositive([7,8,9,11,12])) # 1
