class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        word_memo = [False] * len(s)
        word_memo_visited = [False] * len(s)

        def fit_word(i, remaining_word):

            if len(remaining_word) == 0:
                return True

            if word_memo_visited[i]:
                return word_memo[i]
            
            for word in wordDict:
                if len(word) > len(remaining_word):
                    continue
                if remaining_word[:len(word)] != word:
                    continue
                if fit_word(i + len(word), remaining_word[len(word):]):
                    word_memo[i] = True
                    word_memo_visited[i] = True
                    return True

            word_memo[i] = False
            word_memo_visited[i] = True
            return False
        
        fit_word(0, s)

        return word_memo[0]