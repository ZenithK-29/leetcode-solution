class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        res = []

        def helper(temp):

            if len(temp) == len(nums):
                res.append(temp[:])
                return
            
            for num in nums:

                if num in temp:
                    continue
                
                temp.append(num)
                helper(temp)
                temp.pop()

        helper([])
        return res
        