from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set()

        q = deque()
        l = deque()
        q.append(beginWord)
        l.append(1)
        
        while q:
            current = q.popleft()
            length = l.popleft()
            if current == endWord:
                return length
            if current in visited:
                continue
            visited.add(current)

            for word in wordList:
                for i in range(len(word)):
                    if current[:i] + current[i+1:] == word[:i] + word[i+1:]:
                        q.append(word)
                        l.append(length + 1)
        
        return 0

                