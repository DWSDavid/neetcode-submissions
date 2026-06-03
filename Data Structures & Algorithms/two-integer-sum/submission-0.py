class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # Hashmap = dictionary seen[value] = index, seen[key] = value 
        for i, num in enumerate(nums): # give you the index and value at the same time
            needed = target - num
            if needed in seen:
                return [seen[needed],i]
            
            seen[num] = i # intentionally reverse the order of key and value. Bec
