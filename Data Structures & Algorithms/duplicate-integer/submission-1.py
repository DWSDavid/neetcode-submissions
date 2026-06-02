class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        HashSet = set() in python
        '''
        seen = set();
        for num in nums: #iterate through the set
            if num in seen:
                return True
            seen.add(num)
        return False #should be capitalize

