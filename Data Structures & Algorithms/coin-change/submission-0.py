class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        num_coins = [10001] * (amount + 1)

        num_coins[0] = 0

        for i in range(amount):
            for value in coins:
                if i + value <= amount:
                    num_coins[i + value] = min(num_coins[i + value], num_coins[i] + 1)
        
        if num_coins[-1] == 10001:
            return -1
        
        return num_coins[-1]