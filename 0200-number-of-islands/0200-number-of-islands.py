class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        ROW = len(grid)
        COLUMNS = len(grid[0])
        q = deque()
        visited = set()
        islands = 0

        def bfs(r,c):

            q.append((r, c))
            visited.add((r, c))

            direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            while q:

                row, col = q.pop()

                for dr, dc in direction:

                    nr, nc = row + dr, col + dc

                    if 0 <= nr < ROW and 0 <= nc < COLUMNS and grid[nr][nc] == "1" and (nr, nc) not in visited:

                        q.append((nr, nc))
                        visited.add((nr, nc))



        for r in range(ROW):
            for c in range(COLUMNS):

                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands +=1
        
        return islands
