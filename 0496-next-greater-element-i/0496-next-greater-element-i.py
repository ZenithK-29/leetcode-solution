class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        

        stack = []
        res = [-1] * len(nums2)

        mapped = defaultdict(int)
        output = []

        for i in range(len(nums2)):

            num = nums2[i]

            while stack and num > stack[-1][0]:

                value, idx = stack.pop()
                res[idx] = num

            
            stack.append([num, i])

        for j in range(len(nums2)):
            mapped[nums2[j]] = res[j]
        
        for i in range(len(nums1)):

            if nums1[i] in mapped:
                output.append(mapped[nums1[i]])


        return output