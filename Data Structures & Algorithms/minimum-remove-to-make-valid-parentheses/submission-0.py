class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        # Read forward
        count_forward = 0
        new_s = ""

        for i in range(len(s)):
            if s[i] == "(":
                count_forward += 1
            if not s[i] == ")":
                new_s += s[i]
            else:
                if count_forward > 0:
                    new_s += s[i]
                    count_forward -= 1

        print(new_s)

        # Read backward
        count_backward = 0
        res = ""

        for i in range(len(new_s) - 1, -1, -1):
            if new_s[i] == ")":
                count_backward += 1
            if not new_s[i] == "(":
                res += new_s[i]
            else:
                if count_backward > 0:
                    res += new_s[i]
                    count_backward -= 1
            
            print(count_backward, i, res[::-1])
        
        return res[::-1]