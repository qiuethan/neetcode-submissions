class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        if len(digits) == 0:
            return []

        res = []

        def generate_next(current_str, remaining_digits):
            if len(remaining_digits) == 0:
                res.append(current_str)
                return
            
            for i in range(len(nums_to_letters[remaining_digits[0]])):
                generate_next(current_str + nums_to_letters[remaining_digits[0]][i], remaining_digits[1:])
        
        generate_next("", digits)

        return res