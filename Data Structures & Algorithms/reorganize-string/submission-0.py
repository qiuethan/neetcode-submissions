import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        char_counts = {}
        max_heap = []
        last_letter = "1"
        
        for i in range(len(s)):
            if s[i] not in char_counts:
                char_counts[s[i]] = 0
            char_counts[s[i]] += 1
        
        for letter in char_counts:
            heapq.heappush(max_heap, (-char_counts[letter], letter))
        
        output_string = ""

        for i in range(len(s)):
            if len(max_heap) == 0:
                break

            min_letter = heapq.heappop(max_heap)
            min_letter_count = min_letter[0] * -1
            min_letter = min_letter[1]

            if min_letter == last_letter:
                if len(max_heap) == 0:
                    return ""
                new_min_letter = heapq.heappop(max_heap)
                heapq.heappush(max_heap, (-min_letter_count, min_letter))
                min_letter_count = new_min_letter[0] * - 1
                min_letter = new_min_letter[1]

            
            output_string += min_letter
            last_letter = min_letter

            if min_letter_count > 1:
                heapq.heappush(max_heap, (-(min_letter_count - 1), min_letter))
        
        return output_string

        
        