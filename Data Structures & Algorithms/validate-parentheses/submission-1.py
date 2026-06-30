class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == ")":
                if not stack or stack.pop() != "(":
                    return False
            elif s[i] == "}":
                if not stack or stack.pop() != "{":
                    return False
            elif s[i] == "]":
                if not stack or stack.pop() != "[":
                    return False
            else:
                stack.append(s[i])

        return not stack