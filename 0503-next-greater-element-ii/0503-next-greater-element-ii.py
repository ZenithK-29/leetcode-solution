class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        

        stack = []
        res = [-1] * len(nums)

        for i in range(2*len(nums)):

            if i<len(nums):

                num = nums[i]

                while stack and stack[-1][0] < num:
                    value, idx = stack.pop()
                    res[idx] = num

                stack.append([num, i])

            else:
                i = i%len(nums)

                while stack and stack[-1][0] < nums[i]:
                    value, idx = stack.pop()
                    res[idx] = nums[i]
        
        return res

            


