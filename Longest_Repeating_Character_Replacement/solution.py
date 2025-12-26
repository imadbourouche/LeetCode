class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        l = longest = 0
        most_frequent = 0
        for r, ch in enumerate(s):
            freq_map[ch] = freq_map.get(ch, 0) + 1
            most_frequent = max(freq_map.values())
            if (r - l + 1) - most_frequent > k:
                freq_map[s[l]] -= 1 
                l += 1
            longest = max(longest, (r - l + 1))
        return longest

input = "AAAKBBVT"
k = 2
sol = Solution()
print(sol.characterReplacement(input, k))  # Output: 5