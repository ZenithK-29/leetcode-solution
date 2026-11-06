class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operations = "+/-*"
        stack = []

        for el in tokens:

            if el not in operations:
                stack.append(int(el))

            if el == "+":
                second = stack.pop()
                first = stack.pop()
                stack.append(first+second)

            elif el == "-":
                second = stack.pop()
                first = stack.pop()
                stack.append(first-second)

            elif el == "*":
                second = stack.pop()
                first = stack.pop()
                stack.append(first*second)

            elif el == "/":
                second = stack.pop()
                first = stack.pop()

                if first/second > 0:
                    stack.append(first//second)
                else:
                    stack.append(math.ceil(first/second))

        return stack[-1]