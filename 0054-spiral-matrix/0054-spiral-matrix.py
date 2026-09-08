class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        r, c = len(matrix), len(matrix[0])
        
        rowBegin = 0
        colBegin = 0
        rowEnd = r-1
        colEnd = c-1

        ans = []

        while rowBegin <= rowEnd and colBegin <= colEnd:

            for i in range(colBegin, colEnd+1):

                ans.append(matrix[rowBegin][i])
            
            rowBegin+=1

            for i in range(rowBegin, rowEnd+1):

                ans.append(matrix[i][colEnd])
            
            colEnd-=1

            if rowBegin <= rowEnd:

                for i in range(colEnd, colBegin -1, -1):

                    ans.append(matrix[rowEnd][i])
            
                rowEnd -=1
            
            if colBegin <= colEnd:

                for i in range(rowEnd, rowBegin-1, -1):

                    ans.append(matrix[i][colBegin])
                
                colBegin +=1
            
        return ans
        