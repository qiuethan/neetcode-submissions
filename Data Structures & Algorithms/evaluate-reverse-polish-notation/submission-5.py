class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for index, token in enumerate(tokens):
            if token in "+-*/":
                first = s.pop(-1)
                second = s.pop(-1)
                if token == "+":
                    s.append(second + first)
                elif token == "-":
                    s.append(second - first)
                elif token == "*":
                    s.append(second * first)
                else:
                    s.append(int(second / first))
            else:
                s.append(int(token))
        
        return s[0]