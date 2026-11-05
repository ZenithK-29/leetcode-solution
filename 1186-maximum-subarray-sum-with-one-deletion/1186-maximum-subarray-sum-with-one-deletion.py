class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        
        onedelete = float("-inf")
        nodelete = arr[0]

        res = nodelete

        for i in range(1, len(arr)):
            prevnodelete = nodelete
            prevonedelete = onedelete

            nodelete = max(nodelete+arr[i], arr[i])

            onedelete = max(prevonedelete+arr[i], prevnodelete)

            res = max(nodelete, onedelete, res)
        
        return res
            