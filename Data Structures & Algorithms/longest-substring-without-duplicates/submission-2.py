class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        max_longest = 0
        substring = set()


        for R in range(len(s)):
            while s[R] in substring:
                substring.remove(s[L])
                L += 1

            substring.add(s[R])
            actual_long = R - L + 1

            if actual_long > max_longest:
                max_longest = actual_long

        return max_longest