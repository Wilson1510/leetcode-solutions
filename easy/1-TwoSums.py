from typing import List

"""
Complexity:
- Time  : O(n^2)
- Space : O(1)
"""

class Solution:
    # Runtime: 1764 ms
    # Memory Usage: 18.32 MB
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
        return []
    
    # Best time complexity solution (20 ms)
    def twoSumBestTime(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, element in enumerate(nums):
            if target - element in seen:
                return [seen[target - element],index]

            seen[element] = index

    # Best memory complexity solution (17.3 MB)
    def twoSumBestMemory(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(nums)):
            temp1 = nums[i]
            for j in range(i+1, len(nums)):
                temp2 = nums[j]
                if temp1 + temp2 == target:
                    output = [i, j]
        return output


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))
