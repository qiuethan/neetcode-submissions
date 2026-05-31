class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occurences = [0 for i in range(26)]
        
        for letter in s:
            occurences[ord(letter) - ord('a')] += 1
        
        for letter in t:
            occurences[ord(letter) - ord('a')] -= 1

        for count in occurences:
            if not count == 0:
                return False

        return True