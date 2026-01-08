"""
Complexity:
- Time  : O(n^2)
- Space : O(1)
"""
from typing import List

class Solution:
    # Runtime: 495ms
    # Memory Usage: 22.43MB
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []

        for i in range(n - 2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result
            
    # Best time complexity solution (12ms)
    def threeSumBestTime(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        result = []
        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, h = i+1, n-1
            while l < h:
                summ = nums[i]+nums[l]+nums[h]
                if summ == 0:
                    result.append([nums[i],nums[l],nums[h]])
                    l += 1
                    h -= 1
                    while l < h and nums[l] == nums[l-1]:
                        l += 1
                    while l < h and nums[h] == nums[h+1]:
                        h -= 1
                elif summ < 0:
                    l += 1
                else:
                    h -= 1
        return result

    # Best memory complexity solution (17.9MB)
    def threeSumBestMemory(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] > 0:
                break

            left = i + 1
            right = n - 1
            while left < right:
                if nums[left] + nums[right] == -nums[i]:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] < -nums[i]:
                    left += 1
                else:
                    right -= 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
    print(s.threeSum([0, 1, 1])) # []
    print(s.threeSum([0, 0, 0])) # [[0,0,0]]