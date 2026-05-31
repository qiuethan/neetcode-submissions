class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()

        alphanumeric = "qwertyuiopasdfghjklzxcvbnm1234567890"

        clean = ""
        for letter in s:
            if letter in alphanumeric:
                clean += letter


        left = 0
        right = len(clean) - 1

        while(left < right):
            if clean[left] != clean[right]:
                return False
            left += 1
            right -= 1

        return True
