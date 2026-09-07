class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}

        for index in range(len(nums)):
            current_number = nums[index]
            missing_number = target - current_number

            if missing_number in dictionary:
                return [dictionary[missing_number], index]

            dictionary[current_number] = index