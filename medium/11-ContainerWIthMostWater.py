"""
Complexity:
- Time  : O(n)
- Space : O(1)
"""
from typing import List


class Solution:
    # Runtime: 64ms
    # Memory Usage: 29.61MB
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        
        max_area = 0
        while left < right:
            max_area = max((right-left) * min(height[left], height[right]), max_area)
            if height[left] < height[right]:
                left = left + 1  
            else:
                right = right - 1
                
        return max_area
            

    # Best time complexity solution (0ms)
    def maxAreBestTime(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        max_water = 0

        while l < r:
            max_water = max(max_water, (r - l) * min(height[r],height[l]))
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        
        return max_water

    # Best memory complexity solution (21.5MB)
    def maxAreaBestMemory(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        result = 0

        while left < right:
            pillar_height = min(height[left], height[right])
            width = right - left
            volume = width * pillar_height
            result = max(result, volume)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result



if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))
    print(s.maxArea([1,1]))
