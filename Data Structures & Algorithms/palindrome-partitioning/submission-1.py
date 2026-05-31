class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        current_sol = []
        sols = []

        def isPalindrome(s):
            if len(s) == 1:
                return True
            if len(s) == 2:
                return s[0] == s[1]
            
            if s[0] == s[-1]:
                return isPalindrome(s[1:-1])
            else:
                return False
        
        def partition(s):
            if len(s) == 0:
                sols.append([val for val in current_sol])
            for i in range(1, len(s)+1):
                if isPalindrome(s[:i]):
                    current_sol.append(s[:i])
                    partition(s[i:])
                    current_sol.pop(-1)

        partition(s)
        return sols