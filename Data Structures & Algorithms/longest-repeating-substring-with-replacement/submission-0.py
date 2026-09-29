class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_len = 0
        max_f = 0
        L = 0

        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            max_f = max(max_f, count[s[R]])

            while (R - L + 1) - max_f > k:
                count[s[L]] -= 1
                L += 1

            max_len = max(max_len, R - L + 1)

        return max_len