class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {'{':'}', '(':')' , '[':']'}
        stack = []
        for i in s:
            if i in bracket_dict:
                stack.append(bracket_dict[i])
            elif len(stack)> 0 and stack[-1] == i:
                stack.pop()
            else:
                return False
        return len(stack) ==0

        