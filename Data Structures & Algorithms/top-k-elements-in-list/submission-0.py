class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        sortedC = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        ans = []
        i = 0
        for key in sortedC:
            if i < k:
                ans.append(key)
                i+=1
        return ans
        
