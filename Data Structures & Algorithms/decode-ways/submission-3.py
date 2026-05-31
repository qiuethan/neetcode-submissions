class Solution:
    def numDecodings(self, s: str) -> int:
        num_decodings = [0] * len(s)
        calculated_decodings = [False]*len(s)
        s_list = list(s)

        def calculate_num_decodings(i, remaining):
            if len(remaining) == 0:
                return 1
            
            if calculated_decodings[i]:
                return num_decodings[i]

            if remaining[0] == "0":
                num_decodings[i] = 0
                calculated_decodings[i] = True
                return num_decodings[i]
            
            if len(remaining) == 1:
                num_decodings[i] = 1
                calculated_decodings[i] = True
                return num_decodings[i]
            
            if int(remaining[0] + remaining[1]) in range(1, 27):
                num_decodings[i] += calculate_num_decodings(i + 2, remaining[2:])
            
            num_decodings[i] += calculate_num_decodings(i + 1, remaining[1:])

            calculated_decodings[i] = True
            return num_decodings[i]

        calculate_num_decodings(0, s_list)

        print(num_decodings)
        return num_decodings[0]