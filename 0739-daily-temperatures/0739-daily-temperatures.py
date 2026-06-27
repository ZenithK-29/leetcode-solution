class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        

        stack = []
        ans = [0] * len(temperatures)

        for i, t in enumerate(temperatures):

            while stack and t > stack[-1][0]:
                temp, idx = stack.pop()
                ans[idx] = i - idx
            
            stack.append((t, i))
        
        return ans

