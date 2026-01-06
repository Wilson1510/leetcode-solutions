"""
Complexity:
- Time  : O(n)
- Space : O(1)
"""
from typing import List


class Solution:
    # Runtime: 35ms
    # Memory Usage: 28.75MB
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit
            

    # Best time complexity solution (1ms)
    def maxProfitBestTime(self, prices: List[int]) -> int:
        profit = 0
        min = prices[0]
        max = prices[0]

        for i in range(len(prices)):
            if (prices[i] < min):
                min = prices[i]
                max = prices[i]
            if (prices[i] > max):
                max = prices[i]
            diff = max - min
            profit = diff if diff > profit else profit

                
        return profit

    # Best memory complexity solution (22.4MB)
    def maxProfitBestMemory(self, prices: List[int]) -> int:

        # profit=0 
        # mini=prices[0]
        # for i in prices[1:]:
        #     curr = i-mini
        #     if curr>profit:
        #         profit=curr
        #     if i<mini:
        #         mini=i
        # return profit

        profit = 0
        minimum = prices[0]
        while len(prices) >= 1:
            curr = prices.pop(0)
            minimum = curr if curr < minimum else minimum
            new_profit = curr - minimum
            profit = new_profit if new_profit > profit else profit
        return profit


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([7,6,4,3,1]))
