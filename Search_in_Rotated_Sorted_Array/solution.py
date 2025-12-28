class Solution:
    def binary_search(self, arr, target, l, r):
        while l <= r:
            mid = (r + l) // 2
            if arr[mid] == target:
                return mid
            
            if target > arr[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (r - l) // 2 + l
            if nums[mid] > nums[r]:
                l = mid + 1 
            else:
                r = mid
        
        # l is the pivot
        if target >= nums[l] and target <= nums[len(nums) - 1]:
            res = self.binary_search(nums, target, l, len(nums) - 1)
        else:
            res = self.binary_search(nums, target, 0, l - 1)
        return res
    

solution = Solution()
input = [4,5,6,7,0,1,2]
for target in range(0, 10):
    print(target, solution.search(input, target)) 