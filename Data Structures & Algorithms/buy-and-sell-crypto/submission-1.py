class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        right = 0
        lowest = 101
        highest = 0
        maxProfit = 0

        for i in range(len(prices)):
            maxProfit = max(prices[i]-lowest, maxProfit)

            if prices[i] < lowest:
                lowest = prices[i]
        
        

        # while right < len(prices):
        #     if prices[right] > highest:
        #         highest = prices[right]
        #     if prices[right] < lowest:
        #         print(prices[right])
        #         maxProfit = max(highest - lowest, maxProfit)
        #         lowest = prices[right]
        #         highest = prices[right]

        #     right += 1

        # maxProfit = max(highest-lowest, maxProfit)

        return max(0, maxProfit)