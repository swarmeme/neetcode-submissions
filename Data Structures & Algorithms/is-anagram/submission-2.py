class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        met = {}
        for i in s:
            if i in met:
                met[i] += 1
            else:
                met[i] = 1
        for i in t:
            if i in met:
                if met[i] != 0:  
                    met[i] -= 1
            else:
                met[i] = 1
        if sum(met.values()) != 0:
            return False
        return True