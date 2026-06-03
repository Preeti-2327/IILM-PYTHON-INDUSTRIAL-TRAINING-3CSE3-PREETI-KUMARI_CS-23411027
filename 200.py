class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == '0':
                return

            grid[r][c] = '0'  # mark visited

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        islands = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i, j)

        return islands
