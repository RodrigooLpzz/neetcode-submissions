class Solution:
    def trap(self, heights: List[int]) -> int:
        max_left = [0] * len(heights)
        max_right = [0] * len(heights)

        left_max = 0
        for i in range(len(heights)):
            max_left[i] = left_max
            if heights[i] > left_max:
                left_max = heights[i]

        right_max = 0
        for i in range(len(heights) - 1, -1, -1):
            max_right[i] = right_max
            if heights[i] > right_max:
                right_max = heights[i]

        trapping = 0
        for i in range(len(heights)):
            bottle_neck = min(max_left[i], max_right[i])
            result = bottle_neck - heights[i]

            if result < 1:
                continue
            trapping += result

        return trapping