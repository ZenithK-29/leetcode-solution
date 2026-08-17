class Solution:
    def fib(self, n: int) -> int:

        #recursive O(N) appraoch using caching/memoization

        # memo = {0:0, 1:1}

        # def f(x):

        #     if x in memo:
        #         return memo[x]
        #     else:
        #         memo[x] = f(x-2) + f(x-1)
        #         return memo[x]
        
        # return f(n)


        #iterative approach

        if n == 0:
            return 0
        if n == 1:
            return 1
        
        prev, curr = 0, 1

        for i in range(2, n+1):
            prev, curr = curr, curr+prev
        
        return curr



        #recursive O(2^n)
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        
        # return self.fib(n-2) + self.fib(n-1)