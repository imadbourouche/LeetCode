from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - minimum)
        return max_profit

input = [7,1,5,3,6,4]
sol = Solution().maxProfit(input)
print(sol)  # Output: 5