class Solution:
    def maxArea(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1

        area = 0
        while L < R:
            width = R - L
            if height[L] > height[R]:
                total_height = height[R]
                R -= 1
            elif height[L] < height[R]:
                total_height = height[L]
                L +=1
            else:
                total_height = height[L]
                R -= 1
                L += 1

            if area < (total_height * width):
                area = total_height * width

        return area