class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()

        for i in nums:
            seen.add(i)

        maxs = 0
        curr = 1
        visited = set()

        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            
            num = nums[i]
            while num + 1 in seen:
                num += 1
                curr += 1

            maxs = max(curr, maxs)
            curr = 1

        return maxs
            
