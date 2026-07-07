class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening_brackets = ['{', '(', '[']
        closing_brackets = ['}',')',']']

        for c in s:
            if c in opening_brackets:
                stack.append(c)
            elif c in closing_brackets:
                if len(stack) > 0:
                    if stack[-1] == '{' and c == '}':
                        stack.pop()
                    elif stack[-1] == '(' and c == ')':
                        stack.pop()
                    elif stack[-1] == '[' and c == ']':
                        stack.pop()
                    else:
                        return False
                else: 
                    return False
        
        if len(stack) == 0:
            return True
        return False