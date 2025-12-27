from typing import List
class Solution:

    # binary search
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] <= nums[r]:
                return nums[l]
            mid = (r  + l) // 2
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid
        return nums[l]


    # Optimized version with lower bound check
    def findMin_lower_bound(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (r - l) // 2 + l
            if nums[mid] > nums[r]:
                l = mid + 1 
            else:
                r = mid
        return nums[l]
    
solution = Solution()
input = [3,4,5,1,2]
print(solution.findMin(input))  # Output: 1