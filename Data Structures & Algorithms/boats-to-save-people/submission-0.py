class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        lp = 0
        rp = len(people) - 1

        count = 0

        while lp <= rp:
            if lp == rp:
                count += 1
                break
            if people[lp] + people[rp] <= limit:
                count += 1
                lp += 1
                rp -= 1
            else:
                count += 1
                rp -= 1
        
        return count