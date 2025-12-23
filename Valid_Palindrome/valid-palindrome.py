def isPalindrome(self, s: str) -> bool:
    s = "".join(c for c in s if c.isalnum())
    s = s.lower()
    lp = 0
    rp = len(s) - 1
    while lp < rp:
        if s[lp] != s[rp]:
            return False
        lp += 1
        rp -= 1
    return True
input = "A man, a plan, a canal: Panama"
print(isPalindrome(None, input))