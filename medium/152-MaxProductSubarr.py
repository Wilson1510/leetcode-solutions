"""
Complexity:
- Time  : O(n)
- Space : O(1)
"""
from typing import List


class Solution:
    # Runtime: 7ms
    # Memory Usage: 20.1MB
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        min_current = max_current = result = nums[0]

        for i in range(1, n):
            temp = min_current
            min_current = min(nums[i], min_current * nums[i], max_current * nums[i])
            max_current = max(nums[i], temp * nums[i], max_current * nums[i])
            result = max(result, max_current)
        return result

    # Best time complexity solution (0ms)
    def maxProductBestTime(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Initialize max_product, min_product, and result with first element
        max_prod = min_prod = result = nums[0]
        
        # Iterate over the array starting from index 1
        for num in nums[1:]:
            if num < 0:
                # Swap max_prod and min_prod when num is negative
                max_prod, min_prod = min_prod, max_prod
            
            # Update max_prod and min_prod
            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)
            
            # Update result
            result = max(result, max_prod)

    # Best memory complexity solution (17.3MB)
    def maxProductBestMemory(self, nums: List[int]) -> int:
        res=max(nums)
        curmax,curmin=1,1
        for i in nums:
            if i==0:
                curmin,curmax=1,1
                continue
            temp=curmax*i
            curmax=max(curmax*i,curmin*i,i)
            curmin=min(temp,curmin*i,i)
            res=max(res,curmax)
        return res      


if __name__ == "__main__":
    s = Solution()

    print(s.maxProduct([2,3,-2,4])) # 6
    print(s.maxProduct([-2,0,-1])) # 0
