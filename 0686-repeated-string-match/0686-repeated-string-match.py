class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        
        n = math.ceil(len(b)/len(a)) #min number of times i have to mult 'a' to get len of b

        na = n * a

        if b in na:
            return n
        
        na = a + na

        if b in na:
            return n+1
        
        return -1