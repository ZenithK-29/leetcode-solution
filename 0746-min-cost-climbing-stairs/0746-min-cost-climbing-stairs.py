class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        #DP soln o(n)

        cost.append(0)
        n = len(cost)

        for i in range(n-3, -1,-1):

            cost[i] = min(cost[i]+cost[i+1], cost[i]+cost[i+2])
        
        return min(cost[0], cost[1])

      
        

        #Recursive O(2^n) sol
        # def dfs(i):

        #     if i>=len(cost):
        #         return 0
            
        #     return cost[i] + min(dfs(i+1), dfs(i+2))
        
        # return min(dfs(0), dfs(1))