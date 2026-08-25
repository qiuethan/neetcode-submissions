class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count = 0

        max_index = min([len(string) for string in strs])

        while count < max_index:
            for string in strs:
                if string[count] != strs[0][count]:
                    return strs[0][:count]
            count += 1
        
        return strs[0][:count]