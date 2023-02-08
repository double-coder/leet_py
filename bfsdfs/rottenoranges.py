from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        r, c = len(grid), len(grid[0])
        queue = deque([])
        freshOrange = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    queue.append([i,j])
                elif grid[i][j] == 1:
                    freshOrange += 1
        
        m = 0
        while len(queue) > 0:
            coords = queue[0]
            queue.popleft()

            x, y = coords[0], coords[1]
            for _, dir in enumerate([[0,1], [1,0], [-1,0], [0,-1]]):
                newx, newy = x + dir[0], y + dir[1]
                if newx >= 0 and newy >= 0 and newx < r  and newy < c and grid[newx][newy] == 1:
                    queue.append([newx, newy])
                    grid[newx][newy] = 2
                    freshOrange -= 1
            
            m += 1    
        
        if freshOrange > 0:
            return -1
        
        return m