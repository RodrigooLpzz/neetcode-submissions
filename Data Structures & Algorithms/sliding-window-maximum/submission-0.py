class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # almacena índices en orden de valor monótonamente
        L = 0

        for R in range(len(nums)):
            # Descartar valores más pequeños del final
            while q and nums[q[-1]] < nums[R]:
                q.pop()
            q.append(R)

            # Descartar del frente si quedó fuera de la ventana
            if L > q[0]:
                q.popleft()

            # Una vez alcanzado el tamaño k, registrar el máximo actual
            if (R + 1) >= k:
                output.append(nums[q[0]])
                L += 1

        return output