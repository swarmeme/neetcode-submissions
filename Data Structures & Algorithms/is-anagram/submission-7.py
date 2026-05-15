class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        for i in s:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        
        for i in t:
            if i in seen:
                seen[i] -= 1
            else:
                return False
            
        for i in seen.values():
            if i != 0:
                return False
        
        return True

        #ccbb ccbc [2,2] > [0,2] > [0,1] > [0,1]
