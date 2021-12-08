# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
# You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# 
# Return the max sliding window.
# 
# Example 1:
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# 
# 
# Example 2:
# 
# Input: nums = [1], k = 1
# Output: [1]
# 
# Example 3:
# 
# Input: nums = [1,-1], k = 1
# Output: [1,-1]
# 
# Example 4:
# 
# Input: nums = [9,11], k = 2
# Output: [11]
# 
# Example 5:
# 
# Input: nums = [4,-2], k = 2
# Output: [4]
# 
# 
# Approach 1: 
# 
# As you move the window, 
# (a) check the leftmost number that's not part of the window anymore. Was that the max?
# If yes, we will have to find the new max
# (b) check the rightmost number which is the newest addition to the window. Compare that to the current_max and 
# update current_max accordingly.
# 
# This solution TLEs for extremely huge inputs.

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        curr_max = max(nums[:k])
        max_arr = [curr_max]
        for i in range(k, len(nums)):
            if nums[i-k] == curr_max:
                curr_max = max(nums[i-k+1:i])
            curr_max = max(curr_max, nums[i])
            max_arr.append(curr_max)
        return max_arr


# Approach 2: Dynamic programming
# 
# The idea is to split an input array into blocks of k elements. The last block could contain less elements if n % k != 0.
# 
# Iterate along each block in the array in the direction left->right and build an array left_to_right, where the current index has the 
# maximum number you've encountered till now.
# 
# Do the same within each block going right to left. Call that array right_to_left.
# 
# Build an output array as max(right_to_left[i], left_to_right[i + k - 1]) for i in range (0, n - k + 1).
# 


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        left2right=[]
        right2left=[None for n in nums]
        for left in range(0,len(nums),k):
            max1=nums[left]
            left2right.append(max1)
            for right in range(left+1,min(left+k,len(nums))):
                max1=max(max1,nums[right])
                left2right.append(max1)
            right2=min(left+k, len(nums))
            max2=nums[right2-1]
            for left2 in reversed(range(left,right2)):
                max2=max(max2,nums[left2])
                right2left[left2]=max2
        for left in range(len(nums)-k+1):
            ans.append(max(left2right[left+k-1],right2left[left]))
        return ans
