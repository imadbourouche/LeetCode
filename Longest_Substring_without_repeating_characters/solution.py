class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        l = r = longest = 0
        while r < len(s):
            if s[r] in char_index:
                if char_index[s[r]] < l:
                    char_index[s[r]] = r
                    r += 1
                else:
                    l = char_index[s[r]]+ 1
                    del char_index[s[r]]
            else:
                char_index[s[r]] = r
                r += 1
            longest = max(longest, r - l)
        return longest

input = "abcabcbb"
sol = Solution()
print(sol.lengthOfLongestSubstring(input))  # Output: 3