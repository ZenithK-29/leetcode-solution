class Solution:
    def beautySum(self, s: str) -> int:
        
        result = 0

        for i in range(len(s)):
            count = {}
            for j in range(i, len(s)):

                count[s[j]] = count.get(s[j], 0) + 1

                min_values = min(count.values())
                max_values = max(count.values())

                result = result + (max_values - min_values)

        return result
