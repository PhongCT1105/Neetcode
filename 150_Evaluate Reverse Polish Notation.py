class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        ope = ['*', '/', '+', '-']
        stack = []

        for token in tokens:
            if token == '*':
                cal = stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(cal)
            elif token == '/':
                cal = int(stack[-2] / stack[-1]) if stack[-2] * stack[-1] >= 0 else -(-stack[-2] // stack[-1])
                stack.pop()
                stack.pop()
                stack.append(cal)

            elif token == '+':
                cal = stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(cal)

            elif token == '-':
                cal = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(cal)
            else: 
                stack.append(int(token))

        return stack[0]
