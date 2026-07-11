class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operators = "+-/*"

        for i in range(len(tokens)):
            
            el = tokens[i]

            if el in operators:

                num2 = stack.pop()
                num1 = stack.pop()

                if el == "+":
                    stack.append(num1 + num2)
                elif el == "-":
                    stack.append(num1 - num2)
                elif el == "*":
                    stack.append(num1 * num2)
                elif el == "/":
                    stack.append(int(num1 / num2))
        
            else:
                stack.append(int(el))
        
        return stack[-1]