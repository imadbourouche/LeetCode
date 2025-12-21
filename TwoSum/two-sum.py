from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solutions = {}
        for i in range(len(nums)):
            current_element = nums[i]
            if current_element in solutions:
                return [solutions[current_element], i]
            else:
                difference = target - current_element
                solutions[difference] = i
        return []
