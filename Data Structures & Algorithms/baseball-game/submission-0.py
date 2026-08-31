class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # D = 2x (double the prev score)
        # C = x invalid? remove if not int, C, or D
        stack = []

        for op in operations:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                stack.append(stack[-1] * 2)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)
