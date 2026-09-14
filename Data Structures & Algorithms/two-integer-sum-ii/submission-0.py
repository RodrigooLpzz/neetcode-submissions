class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left_pointer = 0
        right_pointer = len(nums) - 1

        while left_pointer < right_pointer:
            if nums[left_pointer] + nums[right_pointer] > target:
                right_pointer -= 1
            elif nums[left_pointer] + nums[right_pointer] < target:
                left_pointer += 1
            elif nums[left_pointer] + nums[right_pointer] == target:
                return [left_pointer + 1, right_pointer + 1]