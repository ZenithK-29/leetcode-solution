class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        stack = []
        ans = [-1] * len(nums2)

        for i, num in enumerate(nums2):

            while stack and num > stack[-1][0]:
                el, idx = stack.pop()
                ans[idx] = num
            
            stack.append((num, i))

        mappings = {}    
        res = []

        for i in range(len(nums2)):
            mappings[nums2[i]] = ans[i]
        
        for num in nums1:
            res.append(mappings[num])

        return res