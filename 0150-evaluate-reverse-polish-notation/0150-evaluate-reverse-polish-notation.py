class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_stack = []

        operators = "+-*/"

        for t in tokens:
            if t not in operators:
                op_stack.append(int(t))
            else:
                x1 = op_stack.pop()
                x2 = op_stack.pop()

                if t == '+':
                    res = x2 + x1
                elif t == '-':
                    res = x2 - x1
                elif t == '*':
                    res = x2 * x1
                elif t == '/':
                    res = int(x2 / x1) 
            

                op_stack.append(res)

        return op_stack.pop()