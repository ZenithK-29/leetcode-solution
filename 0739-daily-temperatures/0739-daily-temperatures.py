class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0] * len(temperatures)

        j = 0

        while j < len(temperatures):

            temp = temperatures[j]

            while stack and stack[-1][0] < temp:
                value, idx = stack.pop()

                res[idx] = j - idx
            
            stack.append([temp, j])

            j+=1
        
        return res
