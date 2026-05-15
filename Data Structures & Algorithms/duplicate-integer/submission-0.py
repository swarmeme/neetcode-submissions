class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        met = set()
        for i in nums:
            if i in met:
                return True
            met.add(i)
        return False