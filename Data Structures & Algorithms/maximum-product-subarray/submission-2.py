class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        product_dp = [[0]*len(nums) for i in nums]
        calculated_dp = [[False]*len(nums) for i in nums]

        for i in range(len(nums)):
            product_dp[i][i] = nums[i]
            calculated_dp[i][i] = True

        def calculate_product(start, end):
            
            if calculated_dp[start][end]:
                return product_dp[start][end]
            
            product_dp[start][end] = calculate_product(start, end-1) * nums[end]

            calculated_dp[start][end] = True
        
            return product_dp[start][end]

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                calculate_product(i, j)

        max_product = nums[0]

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                max_product = max(product_dp[i][j], max_product)

        print(product_dp)

        return max_product

