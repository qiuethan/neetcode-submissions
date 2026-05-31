class Solution:
    
    def timeToEnd(self, target, position, speed):
        return (target-position)/speed
    
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_to_end = {}

        for i in range(len(position)):
            time_to_end[position[i]] = self.timeToEnd(target, position[i], speed[i])
        
        position.sort(reverse=True)

        fleets = 0
        front_time_to_end = 0

        for i in position:
            if time_to_end[i] > front_time_to_end:
                front_time_to_end = time_to_end[i]
                fleets += 1
        
        return fleets


        

