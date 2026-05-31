from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = deque()

        corresponding = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in "({[":
                parentheses.append(char)
            else:
                if len(parentheses) == 0:
                    return False
                if corresponding[char] != parentheses.pop():
                    return False
        
        if len(parentheses) != 0:
            return False

        return True
                