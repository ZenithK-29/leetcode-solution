class Solution:
    def climbStairs(self, n: int) -> int:

        #iterative O(n) soln

        if n<=2:
            return n
        
        one, two = 1, 1

        for i in range(n-1):
            two, one = one, one+two
        
        return one

        
        #recursive O(2^n)
        # def dfs(i):

        #     if i > n:
        #         return 0
        #     if i == n:
        #         return 1
            
        #     return dfs(i+1) + dfs(i+2)
        
        # return dfs(0)