class Solution:
    def countSubstrings(self, s: str) -> int:
        palindrome_dp = [[False] * len(s) for row in s]
        calculated_dp = [[False] * len(s) for row in s]

        for i in range(0, len(s)):
            palindrome_dp[i][i] = True
            calculated_dp[i][i] = True
        
        for i in range(0, len(s) - 1):
            if s[i] == s[i + 1]:
                palindrome_dp[i][i + 1] = True
            calculated_dp[i][i+1] = True

        def calculate_palindrome(start, end):

            if calculated_dp[start][end]:
                return palindrome_dp[start][end]

            if s[start] != s[end]:
                calculated_dp[start][end] = True
                return False
            
            palindrome_dp[start][end] = calculate_palindrome(start + 1, end - 1)
            calculated_dp[start][end] = True

            return palindrome_dp[start][end]
            
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                calculate_palindrome(i, j)

        count_palindromes = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                if palindrome_dp[i][j]:
                    count_palindromes += 1
        
        return count_palindromes
                        