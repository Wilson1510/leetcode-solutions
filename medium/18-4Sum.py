"""
Complexity:
- Time  : O(n^3)
- Space : O(1)
"""
from typing import List


class Solution:
    # Runtime: 35ms
    # Memory Usage: 19.49MB
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                min_sum = nums[i] + nums[j] + nums[j+1] + nums[j+2]
                if min_sum > target:
                    break

                max_sum = nums[i] + nums[j] + nums[n-1] + nums[n-2]
                if max_sum < target:
                    continue

                left, right = j + 1, n - 1

                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif s < target:
                        left += 1
                    else:
                        right -= 1

        return result

    # Best time complexity solution (5ms)
    def fourSumBestTime(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                left = j+1
                right = len(nums)-1
                while left < right:
                    num = nums[i] + nums[j] + nums[left] + nums[right]
                    if num == target:
                        res.add((nums[i],nums[j],nums[left],nums[right]))
                        left += 1
                        right -= 1
                    elif num > target:
                        right -= 1
                    else:
                        left += 1 
        return list(res)

    # Best memory complexity solution (16.8MB)
    def fourSumBestMemory(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        nums.sort()
        # a,b,l,r
        for a in range(len(nums)):
            if a>0 and nums[a]==nums[a-1]:
                continue
            if a == len(nums)-3:
                break
            for b in range(a+1, len(nums)):
                if b > a+1 and nums[b] == nums[b-1]:
                    continue
                if b == len(nums)-2:
                    break
                l,r = b+1, len(nums)-1
                while l<r:
                    temp = nums[a] + nums[b] + nums[l] + nums[r]
                    if temp > target:
                        r-=1
                    elif temp < target:
                        l+=1
                    else:
                        ret.append([nums[a], nums[b], nums[l], nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
    print(s.fourSum([2, 2, 2, 2, 2], 8))
    print(s.fourSum([0, 0, 0, 0], 0))
    print(s.fourSum([-2, -1, -1, 1, 1, 2, 2], 0))