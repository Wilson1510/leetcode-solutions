"""
Complexity:
- Time  : O(n)
- Space : O(1)
"""
from typing import List


class Solution:
    # Runtime: 35ms
    # Memory Usage: 31.43MB
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = maxSum

        for i in range(1, len(nums)):
            if currentSum < 0 and currentSum < nums[i]:
                currentSum = nums[i]
            else:
                currentSum += nums[i]
            maxSum = max(maxSum, currentSum)

        return maxSum

    # Best time complexity solution (2ms)
    def maxSubArrayBestTime(self, nums: List[int]) -> int:
        # Tương đương "largest" trong code bạn đưa
        current_sum = float('-inf')
        # Tương đương "second_largest" = best overall
        best_sum = float('-inf')

        for x in nums:
            # if → elif kiểu giống code largest / second_largest
            if current_sum < 0:
                current_sum = x          # bắt đầu subarray mới
            else:
                current_sum += x         # tiếp tục subarray hiện tại

            # cập nhật best_sum (giống second_largest = largest)
            if current_sum > best_sum:
                best_sum = current_sum

        return best_sum

    # Best memory complexity solution (28.4MB)
    def maxSubArrayBestSolution(self, nums: List[int]) -> int:
        curmax = nums[0]
        cursum = nums[0]
        for i in range(1, len(nums)):
            # if nums[i]>cursum:
            #     cursum=nums[i]
            # else:
            #     cursum +=nums[i]
            cursum=max(nums[i], nums[i]+cursum)
            curmax=max(curmax,cursum)
                # curmax=cursum

            print(f'cursum, curmax: {cursum, curmax}')

        return curmax


if __name__ == "__main__":
    s = Solution()

    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
    print(s.maxSubArray([1])) # 1
    print(s.maxSubArray([5,4,-1,7,8])) # 23
    print(s.maxSubArray([-2, 1])) # 1
