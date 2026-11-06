class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for br in s:

            if br in brackets:
                if stack and stack[-1] == brackets[br]:
                    stack.pop()
                
                else:
                    return False
            
            else:
                stack.append(br)
        
        return True if not stack else False