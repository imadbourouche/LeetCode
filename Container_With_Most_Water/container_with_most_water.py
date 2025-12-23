from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_space = 0
        while l < r :
            tmp_space = (r - l) * min(height[l], height[r])
            if  tmp_space > max_space: 
                max_space = tmp_space
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_space

input = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(input))  # Expected output: 49
