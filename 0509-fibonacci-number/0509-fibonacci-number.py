class Solution:
    def fib(self, n: int) -> int:

        memo = {0:0, 1:1}

        def f(x):

            if x in memo:
                return memo[x]
            
            memo[x] = f(x-2) + f(x-1)
            return memo[x]
        
        return f(n)



        #Recusive O(2^n) soln
        # if n == 0:
        #     return 0
        
        # if n == 1:
        #     return 1
        
        # return self.fib(n-2) + self.fib(n-1)