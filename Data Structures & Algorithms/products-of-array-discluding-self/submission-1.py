class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            prod = 1 # 1 instead of 0
            for j in range(len(nums)):
                if j!=i:
                    prod*= nums[j]
            result.append(prod)
        return result
