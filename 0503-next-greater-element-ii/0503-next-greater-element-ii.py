class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        

        stack = []
        res = [-1] * len(nums)
        n= len(nums)

        for i in range(2*n):

            idx = i%n
            num = nums[idx]

            while stack and stack[-1][0] < num:
                value, index = stack.pop()
                res[index] = num
            
            if i < n:
                stack.append([num, idx])

        
        return res

            


