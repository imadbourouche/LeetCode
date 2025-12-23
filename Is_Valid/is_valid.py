def isValid(self, s: str) -> bool:
    stack = []
    for i in s:
        if i in ['(', '{', '[']:
            stack.append(i)
        else:
            if not stack:
                return False
            c = stack.pop()
            if (i == ')' and c != '(') or (i == '}' and c != '{') or (i == ']' and c != '['):
                return False
    if stack:
        return False
    return True

input = "({}})"
print("Is valid", isValid(0, input))