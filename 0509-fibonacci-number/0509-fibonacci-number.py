class Solution:
    def fib(self, n: int) -> int:
        
        dp = {0:0, 1:1}

        if n == 0:
            return 0
        if n == 1:
            return 1

        if n in dp:
            return dp[n]

        a1 = self.fib(n-1)
        a2 = self.fib(n-2)

        dp[n] = a1 + a2
        
        return dp[n]