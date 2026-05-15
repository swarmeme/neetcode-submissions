class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        r = 0
        s = []
        while l < len(word1) and r < len(word2):
            s.append(word1[l])
            s.append(word2[r])
            l += 1
            r += 1
        s.append(word1[l:])
        s.append(word2[r:])
        return "".join(s)