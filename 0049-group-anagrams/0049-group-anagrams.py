class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)
        output = []

        for word in strs:

            sort_key = "".join(sorted(word))

            res[sort_key].append(word)

        for k in res:

            output.append(res[k])
        
        return output

