class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)


        for word in strs:

            sort_key = "".join(sorted(word))

            res[sort_key].append(word)

       
        
        return list(res.values())

