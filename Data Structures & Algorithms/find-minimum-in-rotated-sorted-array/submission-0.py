class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        L, R = 0, len(nums) - 1

        while L <= R:
            # Si la ventana ya está completamente ordenada
            if nums[L] < nums[R]:
                res = min(res, nums[L])
                break

            mid = (L + R) // 2
            res = min(res, nums[mid])

            # ¿mid está en la porción ordenada izquierda?
            if nums[mid] >= nums[L]:
                L = mid + 1
            else:
                R = mid - 1

        return res