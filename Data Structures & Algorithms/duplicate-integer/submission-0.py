class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        duplicates = set()
        for i in nums:
            if i in seen:
                duplicates.add(i)
                return True
            else:
                seen.add(i)
        return False