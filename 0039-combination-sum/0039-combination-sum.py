class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        
        res = []

        def helper(idx, temp, summ):

            if summ == target:
                res.append(temp[:])
                return
            
            if idx > len(candidates) - 1:
                return
            

            helper(idx+1, temp, summ)

            if summ + candidates[idx] <= target:

                summ += candidates[idx]
                temp.append(candidates[idx])
                helper(idx, temp, summ)

                summ-=candidates[idx]
                temp.pop()
            
        helper(0, [], 0)
        return res
            