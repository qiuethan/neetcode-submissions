class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = []
        indexes = []
        output = [0]*len(temperatures)

        for index, temp in enumerate(temperatures):
            while len(temps) != 0:
                if temp > temps[-1]:
                    temps.pop(-1)
                    prev_index = indexes.pop(-1)

                    output[prev_index] = index - prev_index
                else:
                    break
            temps.append(temp)
            indexes.append(index)

        return output
