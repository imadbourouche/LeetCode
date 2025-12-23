from typing import List
class Solution:
    # optimal solution using sorting and two pointers
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break
 
            if i > 0 and a == nums[i-1]:
                continue

            l, r = i+1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0 :
                    r -= 1 
                elif threeSum < 0 :
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
    
    # Personal solution less optimal solution using hash map
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        res=[]
        seen = set()
        for i in range(len(nums)):
            a = nums[i]
            if a in seen:
                continue
            target = 0 - a

            # two sum problem
            map_target = {}
            local_seen = set()

            for j in range(len(nums)):
                if j == i:
                    continue
                c = nums[j]
                if c in map_target:
                    b = map_target[c]
                    sol = [a, b, c]
                    if b not in local_seen and c not in local_seen:
                        if (a not in seen) and (b not in seen) and (c not in seen):
                            res.append(sol)
                            local_seen.add(b)
                            local_seen.add(c)
                    del map_target[nums[j]]
                else:
                    k_target = target - nums[j]
                    map_target[k_target] = nums[j]
            seen.add(a)
        return res


# Example usage:
sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))
print(sol.threeSum2([-1,0,1,2,-1,-4]))