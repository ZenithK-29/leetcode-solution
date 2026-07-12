class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLUMNS = len(grid), len(grid[0])
        fresh = 0
        time = 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLUMNS):

                if grid[r][c] == 2:   #to add rotten oranges to queue
                    q.append([r,c])
                elif grid[r][c] == 1: #to check for total no if fresh oranges
                    fresh +=1
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]] #down, up, right, left

        while q and fresh > 0:

            qLen = len(q)

            for _ in range(qLen):

                row, col = q.popleft()

                for dr, dc in directions:

                    nr = row + dr
                    nc = col + dc

                    if nr < 0 or nc < 0 or nc >= COLUMNS or nr >= ROWS or grid[nr][nc] != 1:
                        continue
                    
                    grid[nr][nc] = 2
                    q.append([nr, nc])
                    fresh -=1
                
            time +=1
        
        return time if fresh == 0 else -1

