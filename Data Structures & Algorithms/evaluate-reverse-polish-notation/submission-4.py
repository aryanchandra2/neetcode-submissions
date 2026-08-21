class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        val = 0
        for c in tokens:
            if c == "+":
                val = stack.pop() + stack.pop()
                stack.append(val)
            elif c == "-":
                right = stack.pop()
                left = stack.pop()
                val = left - right
                stack.append(val)
            elif c == "*":
                val = stack.pop() * stack.pop() 
                stack.append(val) 
            elif c == "/":
                right = stack.pop()
                left = stack.pop()
                val = int(float(left) / right)
                stack.append(val)
            else:
                stack.append(int(c))
        return stack.pop()
