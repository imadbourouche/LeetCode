class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []
        def backtrack(i, sum_result):
            if sum_result == target:
                res.append(sol[:])
                return
            if sum_result > target or i >= len(candidates):
                return

            sol.append(candidates[i])
            backtrack(i, sum_result + candidates[i])
            sol.pop()

            backtrack(i + 1, sum_result)
            
        backtrack(0, 0)
        return res