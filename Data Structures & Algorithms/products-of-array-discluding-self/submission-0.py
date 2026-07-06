class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = [1] * len(nums)
        prefix = 1
        suffix = 1
        length = len(nums)
        for i in range(length):
            prod[i] = prefix
            prefix *= nums[i]
        for i in range(length - 1, -1, -1):
            prod[i] *= suffix
            suffix *= nums[i]
        return prod