"""
Complexity:
- Time  : O(n)
- Space : O(1)
"""
from typing import List


class Solution:
    # Runtime: 0ms
    # Memory Usage: 20.3MB
    def missingNumber(self, nums: List[int]) -> int:
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)

    # Best time complexity solution (8ms)
    def missingNumberBestTime(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = (n * (n + 1)) // 2
        return expected_sum - sum(nums)

    # Best memory complexity solution (17.9MB)
    def missingNumberBestMemory(self, nums: List[int]) -> int:
        for num in range(0, len(nums) + 1):
            if num not in nums:
                return num
        return 0


if __name__ == "__main__":
    s = Solution()

    print(s.missingNumber([3, 0, 1]))  # 2
    print(s.missingNumber([0, 1]))  # 2
    print(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 8
