class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        q = deque()
        ROWS = len(grid)
        COLUMNS = len(grid[0])
        fresh = 0
        minutes = 0

        for r in range(ROWS):
            for c in range(COLUMNS):

                if grid[r][c] == 2:
                    q.append((r, c))
                
                elif grid[r][c] == 1:
                    fresh +=1
        

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while q and fresh > 0:

            qLen = len(q)

            for _ in range(qLen):

                row, col = q.popleft()

                for dr, dc in directions:

                    nr, nc = row + dr, col + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLUMNS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -=1
            
            minutes +=1
        
        return minutes if fresh == 0 else -1
