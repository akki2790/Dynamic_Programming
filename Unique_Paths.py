# 62. Unique Paths
# 
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?
# 
# Input: m = 3, n = 7
# Output: 28
# 
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
# 
# Input: m = 7, n = 3
# Output: 28
# 
# Dynamic Programming Approach:
# Each cell in the DP grid represents the numnber of ways/paths to get to that cell.
# First row and first col ll be initialized by 1. (to make it faster)
# For inner cells that have the option left and above ll add up both the values
# 

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m = rows and n = cols
        dp = [[1]*n for row in range(m)]
        
        for row in range(1,m):
            for col in range(1,n):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
        
        return dp[-1][-1]
