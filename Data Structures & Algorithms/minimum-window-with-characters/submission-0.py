class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_length = len(s) + 1
        min_left = 0
        min_right = 0

        count_t = [0]*(ord('z') - ord('A') + 1)
        count_s = [0]*(ord('z') - ord('A') + 1)

        def add_count(lst, char):
            lst[ord(char) - ord('A')] += 1
        
        def sub_count(lst, char):
            lst[ord(char) - ord('A')] -= 1

        def check_l1_in_l2(l1, l2):
            for i in range(len(l1)):
                if l1[i] > l2[i]:
                    return False
            
            return True

        left = 0
        right = 0

        for i in range(len(t)):
            add_count(count_t, t[i])

        add_count(count_s, s[0])

        while right < len(s):
            print(left, right, count_s, count_t)
            if check_l1_in_l2(count_t, count_s):
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_left = left
                    min_right = right 
                sub_count(count_s, s[left])
                left += 1
            else:
                right += 1
                if right >= len(s):
                    break
                add_count(count_s, s[right])

        if min_length == len(s) + 1:
            return ""

        return s[min_left:min_right + 1]