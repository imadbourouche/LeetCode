from typing import List
def minCost(self, s: str, cost: List[int]) -> int:
    max_cost = sum(cost)
    min_cost = max_cost
    map_char = {}
    for i, c in enumerate(s):
        map_char[c] = map_char.get(c, 0) + cost[i] # accumulate cost per character
        cost_i = max_cost - map_char[c] # cost to let the group of character c remain
        if min_cost > cost_i:
            min_cost = cost_i
    return min_cost 

input = "abaac"
cost = [1,2,3,4,5]
print(minCost(None, input, cost))  # Expected output: 7