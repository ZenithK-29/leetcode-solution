class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        
        res = [-1] * len(nums1)
        stack = []
        nums1Idx = {num: i for i, num in enumerate(nums1)}

        for i in range(len(nums2)):

            curr = nums2[i]

            while stack and stack[-1] < curr:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = curr

            if curr in nums1Idx:
                stack.append(curr)

        return res 