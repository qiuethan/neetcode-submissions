class Solution:
    
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(s):
            if len(s) <= 1:
                return True
            
            if s[0] == s[-1]:
                return isPalindrome(s[1:-1])
            
            return False

        if isPalindrome(s):
            return True

        for i in range(len(s)):
            if isPalindrome(s[:i] + s[i+1:]):
                return True
            
        return False