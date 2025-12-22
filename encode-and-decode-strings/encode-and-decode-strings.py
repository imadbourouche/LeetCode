from typing import List

def encode(self, strs: List[str]) -> str:
    res = []
    for s in strs:
        if ',' in s:
            # add \ before ,
            s = s.replace(',', '\\,')
        res.append(s)
        res.append(',')
    return ''.join(res)

def decode(self, s: str) -> List[str]:
    res, i = [], 0
    print(f's: {s}')
    while i < len(s):
        curr = []
        while i < len(s) and s[i] != ',':
            if s[i] == '\\' and i + 1 < len(s) and s[i + 1] == ',':
                curr.append(',')
                i += 2
            else:
                curr.append(s[i])
                i += 1
        res.append(''.join(curr))
        i += 1
    return res

input = ["", "Hel,#lo", "", "World,", "", "Hello\,World"]
encoded = encode(None, input)
print(f'Encoded: {encoded}')
decoded = decode(None, encoded)
print(f'Decoded: {decoded}')