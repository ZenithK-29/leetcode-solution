class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        
        longest_sequence = 0
        s = set(nums)

        for num in s:

            if num - 1 not in s:

                current_num = num
                current_seq = 1

                while current_num + 1 in s:

                    current_num += 1
                    current_seq += 1
                
                longest_sequence = max(longest_sequence, current_seq)
        
        return longest_sequence