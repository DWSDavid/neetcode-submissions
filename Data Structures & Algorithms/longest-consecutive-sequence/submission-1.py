class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # 去重
        longest = 0
        for num in numSet:
            if num - 1 not in numSet: # a very smart line of code
                length = 1
                current = num
                while current+1 in numSet: # in numSet
                    length+=1
                    current += 1
                longest = max(length,longest)
        return longest
