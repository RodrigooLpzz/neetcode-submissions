class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        res = R

        while L <= R:
            k = (L + R) // 2
            hours = sum((p + k - 1) // k for p in piles)

            if hours <= h:
                res = k
                R = k - 1  # Intentar buscar una velocidad aún menor
            else:
                L = k + 1  # Velocidad insuficiente, necesita ir más rápido

        return res