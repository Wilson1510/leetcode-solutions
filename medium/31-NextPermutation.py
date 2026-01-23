"""
Complexity:
- Time  : O(n)
- Space : O(1)
"""
from typing import List


class Solution:
    # Runtime: 0ms
    # Memory Usage: 19.25MB
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i = i - 1

        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j = j - 1
            nums[i], nums[j] = nums[j], nums[i]
        
        nums[i+1:] = reversed(nums[i+1:])

    # Best time complexity solution (0ms)
    def nextPermutationBestTime(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        # finding the first element that breaks the increasing order
        while i >=0 and nums[i] >= nums[i+1]:
            i -= 1
        
        # if we reach the start that means the whole list is descending that is it is the biggest permutation so we just reverse to get smallest (which is the revers)
        if i == -1:
            nums.reverse()
            return
        
        # find the smallest larger number than nums[i] to swap with
        j = n-1
        while nums[j] <= nums[i]:
            j -= 1
        
        # swap 
        nums[i], nums[j] = nums[j], nums[i]

        # reverse the suffix as suffix is always ascending 
        l, r = i+1, n-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1

    # Best memory complexity solution (16.4MB)
    def nextPermutationBestMemory(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1
        n = len(nums)

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i
                break
        
        if index == -1:
            nums.reverse()
            return 
        
        for i in range(n - 1, index, -1):
            if nums[i] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                break
        
        nums[index + 1:] = reversed(nums[index + 1:])


if __name__ == "__main__":
    s = Solution()

    print(s.nextPermutation([1, 2, 3])) # [1, 3, 2]
    print(s.nextPermutation([3, 2, 1])) # [1, 3, 2]
    print(s.nextPermutation([1, 1, 5])) # [1, 5, 1]
