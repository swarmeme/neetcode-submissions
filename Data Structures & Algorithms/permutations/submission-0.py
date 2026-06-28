class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        seen = set()  # Tracks numbers currently in our stack
        stack = []
        res = []

        def dfs():  # No need for arguments here
            # Base case: stack is full, we found a valid permutation
            if len(stack) == len(nums):
                res.append(stack.copy())
                return

            for i in nums:
                # If the number is already used in the current path, skip it
                if i in seen:
                    continue

                # 1. Choose
                stack.append(i)
                seen.add(i)

                # 2. Explore
                dfs()

                # 3. Un-choose (Backtrack)
                stack.pop()
                seen.remove(i)

        dfs()  # Start the recursion
        return res