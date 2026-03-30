class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            match c:
                case '+':
                    a, b = stack.pop(), stack.pop()
                    stack.append(a + b)
                case '-':
                    a, b = stack.pop(), stack.pop()
                    stack.append(b - a)
                case '*':
                    a, b = stack.pop(), stack.pop()
                    stack.append(a * b)
                case '/':
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(b / a))
                case _:
                    stack.append(int(c))

        return stack[0]