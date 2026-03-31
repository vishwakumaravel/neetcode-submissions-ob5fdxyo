class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                # Get the last two scores and add their sum to the stack
                # Check if there are at least two scores
                if len(stack) >= 2:
                    new_score = stack[-1] + stack[-2]
                    stack.append(new_score)
            elif op == "D":
                # Double the previous score and add it to the stack
                # Check if there is at least one score
                if stack:
                    new_score = stack[-1] * 2
                    stack.append(new_score)
            elif op == "C":
                # Invalidate the previous score by removing it
                # Check if there is a score to remove
                if stack:
                    stack.pop()
            else:
                # The operation is a number, so add it to the stack
                stack.append(int(op))
        return sum(stack)

