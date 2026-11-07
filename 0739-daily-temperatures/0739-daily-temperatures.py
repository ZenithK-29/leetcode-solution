class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        
        stack = [0]
        output = [0] * len(temperatures)

        for i in range(1, len(temperatures)):

            temp = temperatures[i]

            while stack and temperatures[stack[-1]] < temp:
                idx = stack.pop()
                output[idx] = i - idx
            
            stack.append(i)
        
        return output