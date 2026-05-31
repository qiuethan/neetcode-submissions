class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            count = [0]*26
            for letter in string:
                count[ord(letter) - ord('a')] += 1
            if str(count) not in anagrams:
                anagrams[str(count)] = []
            anagrams[str(count)].append(string)
        return list(anagrams.values())