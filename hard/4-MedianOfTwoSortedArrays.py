from typing import List

"""
Complexity:
- Time  : O((m + n) * log(m + n))
- Space : O(m + n)
"""


class Solution:
    # Runtime: 0 ms
    # Memory Usage: 17.99 MB
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        
        if len(nums) % 2 == 0:
            return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2
        else:
            return float(nums[len(nums) // 2])
        
    # Best time complexity solution (0 ms)
    def findMedianSortedArraysBestTime(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 +nums2
        length = len(nums)
        nums.sort()
        if length==0:
            return 0
        elif length%2==0:
            return ((nums[length//2 -1] + nums[length//2]) /2)
        else:
            return nums[length//2]

    # Best memory complexity solution (17.2 MB)
    def findMedianSortedArraysBestMemory(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArraysBestMemory(nums2, nums1)
        start, end = 0, m
        while start <= end:
            i = start + (end - start) // 2
            j = (m + n + 1) // 2 - i
            if i > 0 and nums1[i - 1] > nums2[j]:
                end = i - 1
            elif i < m and nums2[j - 1] > nums1[i]:
                start = i + 1
            else:
                max_left = nums1[i - 1] if j == 0 else (nums2[j - 1] if i == 0 else max(nums1[i - 1], nums2[j - 1]))
                if (m + n) % 2 == 1:
                    return max_left
                min_right = nums1[i] if j == n else (nums2[j] if i == m else min(nums1[i], nums2[j]))
                return (max_left + min_right) / 2


if __name__ == "__main__":
    s = Solution()
    print(s.findMedianSortedArrays([1,3], [2]))
    print(s.findMedianSortedArrays([1,2], [3,4]))