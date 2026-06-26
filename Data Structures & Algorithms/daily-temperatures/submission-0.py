class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        stack.append(0)

        res = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                val = stack.pop()
                res[val] = i - val

            stack.append(i)

        return res 


            