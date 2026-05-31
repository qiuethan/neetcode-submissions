class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        visited = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        memo = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]

        def isValid(s1Index, s2Index):
            if s1Index == len(s1) and s2Index == len(s2):
                return True
            
            if s1Index > len(s1) or s2Index > len(s2):
                return False

            if visited[s1Index][s2Index]:
                return memo[s1Index][s2Index]
            
            visited[s1Index][s2Index] = True

            if s1Index < len(s1):
                if s1[s1Index] == s3[s1Index + s2Index]:
                    memo[s1Index][s2Index] = isValid(s1Index + 1, s2Index)
            
            if s2Index < len(s2):
                if s2[s2Index] == s3[s1Index + s2Index]:
                    memo[s1Index][s2Index] = memo[s1Index][s2Index] or isValid(s1Index, s2Index + 1)
            
            return memo[s1Index][s2Index]
        
        if len(s1) + len(s2) != len(s3):
            return False

        return isValid(0,0)