class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) ==0:
            return 0

        minprice = prices[0]
        maxprofit = 0

        for i in range(1,len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            else:
                profit = prices[i] - minprice
                maxprofit = max(maxprofit, profit)

        return maxprofit