class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid or len(grid) == 0:
            return 0

        r = len(grid)
        c = len(grid[0])
        count = 0
        def dfs(x, y):
            if x < 0 or x >= r or y < 0 or y >= c or grid[x][y] == 'W':
                return
            grid[x][y] = 'W'
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 'L': 
                    count += 1
                    dfs(i, j)  

        return count

