class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            seen[s[i]] = seen.get(s[i], 0) + 1
            seen[t[i]] = seen.get(t[i], 0) - 1

        for i in seen.values():
            if i != 0:
                return False
        
        return True

        

        