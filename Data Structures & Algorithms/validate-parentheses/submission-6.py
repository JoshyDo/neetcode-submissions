class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {'}': '{', ')': '(', ']': '['}

        for c in s:
            if c in matching.values():
                stack.append(c)
            elif c in matching:
                if not stack or stack[-1] != matching[c]:
                    return False
                stack.pop()

        return len(stack) == 0