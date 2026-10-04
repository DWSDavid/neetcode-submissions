class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        seen = set()
        islands = 0 
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        for r in range (rows):
            for c in range (cols):
                if grid[r][c] != "1" or (r,c) in seen:
                    continue 
                islands += 1
                seen.add((r,c))
                stack = [(r,c)]
                while stack:
                    cr,cc = stack.pop()
                    for dr,dc in directions:
                        nr,nc = cr + dr, cc + dc
                        if(
                            0 <= nr < rows 
                            and 0 <= nc < cols 
                            and grid[nr][nc] == "1" 
                            and (nr,nc) not in seen
                        ): 
                            seen.add((nr,nc))
                            stack.append((nr,nc))

        return islands