# 63. Unique Paths II ( w/ obstacle in the middle)
# 
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
# An obstacle and space is marked as 1 and 0 respectively in the grid.
# 
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# 
# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1
# 

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rl, cl = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[1] * cl for row in range(rl)]
        #for row in dp:
        #    print (row)
        col_obs ,row_obs = False, False
        for col in range(cl):    # first row sorted
            if obstacleGrid[0][col] == 1:
                col_obs = True
            if col_obs:
                dp[0][col] = 0
        for row in range(rl):	# first col
            if obstacleGrid[row][0] == 1:
                row_obs = True
            if row_obs:
                dp[row][0] = 0
        for row in range(1,rl): # everything inside
            for col in range(1,cl):
                if obstacleGrid[row][col] == 1: # i.e. obstacle
                    dp[row][col] = 0
                else:
                    dp[row][col] = dp[row-1][col] + dp[row][col-1]
        #for row in dp:
        #    print (row)
        return dp[-1][-1]
