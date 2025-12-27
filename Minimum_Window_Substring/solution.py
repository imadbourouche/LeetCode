from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = r = 0
        count_t = Counter(t)
        have = 0 
        need = len(count_t)
        window_counts = {}
        minimum_length = float("inf")
        minimum_window = ""
        for r in range(len(s)):
            if s[r] in count_t:
                window_counts[s[r]] = window_counts.get(s[r], 0) + 1
                if window_counts[s[r]] == count_t[s[r]]:
                    have += 1
            while have == need:
                if (r - l +1) < minimum_length:
                    minimum_length = r - l + 1
                    minimum_window = s[l:r+1]
                if s[l] in window_counts:
                    window_counts[s[l]] -= 1
                    if window_counts[s[l]] < count_t[s[l]]:
                        have -= 1
                l += 1
        return minimum_window

input = "kfgkfkgkfADOBECODEBANCkfgkfkgkf"
t = "ABC"
solution = Solution()
print(solution.minWindow(input, t))  # Expected output: "BANC"