class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        ref = strs[0]

        for i in range(len(ref)):

            for word in strs:

                if i == len(word) or word[i] != ref[i]:
                    return ref[:i]
        

        return ref    