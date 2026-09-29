class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(s) < len(t):
            return ""

        target_count = {}
        for c in t:
            target_count[c] = 1 + target_count.get(c, 0)

        window_count = {}
        have, need = 0, len(target_count)
        res, res_len = [-1, -1], float("inf")
        L = 0

        for R in range(len(s)):
            char = s[R]
            window_count[char] = 1 + window_count.get(char, 0)

            if char in target_count and window_count[char] == target_count[char]:
                have += 1

            while have == need:
                # Actualizar resultado si la ventana actual es más compacta
                if (R - L + 1) < res_len:
                    res = [L, R]
                    res_len = R - L + 1

                # Reducir desde la izquierda
                left_char = s[L]
                window_count[left_char] -= 1
                if left_char in target_count and window_count[left_char] < target_count[left_char]:
                    have -= 1
                L += 1

        L, R = res
        return s[L : R + 1] if res_len != float("inf") else ""