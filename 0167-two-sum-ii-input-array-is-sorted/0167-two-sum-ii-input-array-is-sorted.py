class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        count = {}

        for i in range(len(numbers)):

            el = numbers[i]
            if target - el in count:
                res = [i+1, count[target-el] + 1]
                res.sort()
                return res
            
            count[el] = i
        