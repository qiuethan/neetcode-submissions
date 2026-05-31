class Solution:

    strings = []

    def generateString(self, n: int, current_string: str, open_bracket: int, closed_bracket: int) -> None:

        if closed_bracket < open_bracket:
            return
        
        if n == 0:
            self.strings.append(current_string)
            return
        
        if open_bracket > 0:
            self.generateString(n - 1, current_string + "(", open_bracket - 1, closed_bracket)
        
        if closed_bracket > 0:
            self.generateString(n - 1, current_string + ")", open_bracket, closed_bracket - 1)
        

    def generateParenthesis(self, n: int) -> List[str]:
        self.strings = []

        self.generateString(2*n, "", n, n)

        return self.strings
