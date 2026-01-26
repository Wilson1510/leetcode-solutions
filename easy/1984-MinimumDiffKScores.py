"""
Complexity:
- Time  : O(n log(n))
- Space : O(1)
"""
from typing import List


class Solution:
    # Runtime: 7ms
    # Memory Usage: 19.49MB
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        minimum = float('inf')
        bound = len(nums) - k + 1

        for i in range(bound):
            minimum = min(minimum, nums[i + k - 1] - nums[i])
        return minimum

    # Best time complexity solution (0ms)
    def minimumDifferenceBestTime(self, nums: List[int], k: int) -> int:
        if k==1:
            return 0
        nums.sort()
        min_dif=float('inf')
        for i in range(len(nums)-k+1):
            dif=nums[i+k-1]-nums[i]
            min_dif=min(min_dif,dif)
        return min_dif

    # Best memory complexity solution (19.49MB)
    def minimumDifferenceBestMemory(self, nums: List[int], k: int) -> int:
        if k==1:
            return 0
        nums.sort()
        min_diff=float("inf")
        for i in range(len(nums)-k+1):
            diff=abs(nums[i]-nums[i+k-1])
            min_diff=min(min_diff,diff)
        return min_diff


if __name__ == "__main__":
    s = Solution()

    print(s.minimumDifference([90], 1)) # 0
    print(s.minimumDifference([9,4,1,7], 2)) # 2
    print(s.minimumDifference([1, 2, 100, 101], 3)) # 99
