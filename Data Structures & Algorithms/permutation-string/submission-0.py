class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord("a")] += 1
            s2_count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1

        L = 0
        for R in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # Agregar el carácter de la derecha
            idx = ord(s2[R]) - ord("a")
            s2_count[idx] += 1
            if s2_count[idx] == s1_count[idx]:
                matches += 1
            elif s2_count[idx] == s1_count[idx] + 1:
                matches -= 1

            # Remover el carácter que queda fuera por la izquierda
            idx = ord(s2[L]) - ord("a")
            s2_count[idx] -= 1
            if s2_count[idx] == s1_count[idx]:
                matches += 1
            elif s2_count[idx] == s1_count[idx] - 1:
                matches -= 1

            L += 1

        return matches == 26