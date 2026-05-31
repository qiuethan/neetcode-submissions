class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()

        memo = [[-1] * (amount + 1) for i in range(len(coins))]

        def calculateCombos(i, coinIndex):

            if i == amount:
                return 1

            if coinIndex >= len(coins):
                return 0

            if i > amount:
                return 0

            if memo[coinIndex][i] != -1:
                return memo[coinIndex][i]

            memo[coinIndex][i] = 0

            for index in range(coinIndex, len(coins)):
                memo[coinIndex][i] += calculateCombos(i + coins[index], index)
        
            return memo[coinIndex][i]
        
        if amount == 0:
            return 1

        calculateCombos(0, 0)
        
        return memo[0][0]

