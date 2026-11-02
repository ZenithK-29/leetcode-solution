class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        wordCount = defaultdict(list)

        for word in strs:

            sorted_word = "".join(sorted(word))

            wordCount[sorted_word].append(word)
        
        res = []

        for word in wordCount.values():
            res.append(word)
        
        return res