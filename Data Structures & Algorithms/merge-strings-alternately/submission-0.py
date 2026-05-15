class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        s = ""
        while l < len(word1) and l < len(word2):
            s += word1[l]
            s += word2[l]
            l += 1
        if l < len(word1):
            for i in range(l, len(word1)):
                s += word1[i]
        if l < len(word2):
            for i in range(l, len(word2)):
                s += word2[i]
        return s