class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        
        res = []

        letters_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

        def backtracking(i, temp):

            if len(temp) == len(digits):
                res.append(''.join(temp))
                return 
            
            for letter in letters_map[digits[i]]:

                temp.append(letter)
                backtracking(i+1, temp)

                temp.pop()

        backtracking(0, [])

        return res