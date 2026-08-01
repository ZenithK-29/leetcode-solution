class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        #optimal binary search approach

        def count_func(matrix, n, target):

            row = n-1
            col = 0
            count = 0

            while row >= 0 and col < n:
                if matrix[row][col] <= target:
                    count += row+1
                    col +=1
                else:
                    row -=1

            return count

        n = len(matrix)
        low = matrix[0][0]
        high = matrix[n-1][n-1]

        while low <= high:

            mid = low + (high-low)//2

            count = count_func(matrix, n, mid)

            if count < k:
                low = mid + 1
            
            else:
                high = mid - 1

        return low

       
