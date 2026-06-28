class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        stack = []
        res = []

        def dfs():
            if len(stack) == len(nums):
                res.append(stack.copy())
                return

            for i in nums:
                if i in seen:
                    continue
                
                stack.append(i)
                seen.add(i)

                dfs()

                stack.pop()
                seen.remove(i)

        dfs()

        return res