class Solution:
    def isValid(self, s: str) -> bool:
        
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for br in s:

            if br in mapping:
                if not stack or stack[-1] != mapping[br]:
                    return False
                stack.pop()
            
            else:
                stack.append(br)
        
        return len(stack) == 0