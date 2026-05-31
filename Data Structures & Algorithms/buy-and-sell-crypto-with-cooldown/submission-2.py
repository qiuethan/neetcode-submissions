class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = [-1] * len(prices)
        memo = [[-1] * len(prices) for i in range(len(prices))]

        def calculateProfit(buyIndex):

            if buyIndex >= len(prices):
                return 0

            if profit[buyIndex] == -1:
                for sellIndex in range(buyIndex + 1, len(prices)):
                    if memo[buyIndex][sellIndex] == -1:
                        memo[buyIndex][sellIndex] = prices[sellIndex] - prices[buyIndex] + calculateProfit(sellIndex + 2)
                    profit[buyIndex] = max(profit[buyIndex], memo[buyIndex][sellIndex])
                profit[buyIndex] = max(profit[buyIndex], calculateProfit(buyIndex + 1))
                
            profit[buyIndex] = max(0, profit[buyIndex])

            return profit[buyIndex]
        
        calculateProfit(0)

        return profit[0]

            
