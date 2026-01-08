"""
Complexity:
- Time  : O(n^2)
- Space : O(1)
"""
from typing import List
from math import inf

class Solution:
    # Runtime: 378ms
    # Memory Usage: 19.44MB
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        result = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(total - target) < abs(result - target):
                    result = total
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return target

        return result

    # Best time complexity solution (3ms)
    def threeSumClosestBestTime(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) -2):
            left,right = i+1, len(nums) -1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if abs(target - total) < abs(target - result):
                    result = total
                if total == target:
                    return target
                elif total < target:
                    left+=1
                else:
                    right-=1

        return result

    # Best memory complexity solution (16.8MB)
    def threeSumClosestBestMemory(self, nums: List[int], target: int) -> int:
        nums.sort()
        out = inf
        for i in range(1, len(nums)-1):
            start, end = 0, len(nums)-1
            while end-start>1:
                xx = nums[start]+nums[end]+nums[i]
                if xx == target:
                    return xx
                if abs(target-out)>abs(target-xx):
                    out = xx
                if xx > target:
                    end -= 1
                else:
                    start += 1
                if start == i or end == i:
                    break
        return out


if __name__ == "__main__":
    s = Solution()
    print(s.threeSumClosest([-1, 2, 1, -4], 1)) # 2
    print(s.threeSumClosest([0, 0, 0], 1)) # 0
    print(s.threeSumClosest([1, 1, 1, 0], -100)) # 2
    print(s.threeSumClosest([1, 1, 1, 0], 100)) # 3