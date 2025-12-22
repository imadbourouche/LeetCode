from typing import List

def productExceptSelf(self, nums: List[int]) -> List[int]:
    arr1 = [1] * len(nums)
    for i in range(len(nums) - 1):
        arr1[i+1] = nums[i] * arr1[i]

    tmp = 1
    for i in range(len(nums) - 1, -1, -1):
        if i == 0: break
        tmp = tmp * nums[i]
        arr1[i-1] = tmp * arr1[i-1]

input = [1, 2, 3, 4]
print(productExceptSelf(None, input))  # Expected output: [24, 12, 8, 6]