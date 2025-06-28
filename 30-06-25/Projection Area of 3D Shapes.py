class Solution(object):
    def projectionArea(self, grid):
        result = 0
        zero = 0
        for item in grid:
            for num in item :
                if num == 0 :
                    zero += 1
        result += len(grid) * len(grid[0]) - zero
        n = len(grid[0])
        for i in range(len(grid)) :
            result += max(grid[i])
        transpose = [[row[i] for row in grid] for i in range(n)]
        for i in range(n) :
            result += max(transpose[i])
        return result
        
