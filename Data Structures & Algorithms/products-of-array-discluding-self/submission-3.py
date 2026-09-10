class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_list = []
        prefix_list.append(1)
        for i in range(1, len(nums)):
            new_value = prefix_list[i - 1] * nums[i - 1]
            prefix_list.append(new_value)
      
        suffix_list = [1] * (len(nums))
        for i in range(len(nums) - 2, -1, -1):
            new_value = suffix_list[i + 1] * nums[i + 1]
            suffix_list[i] = new_value

        result = []
        for i in range(len(nums)):
            result.append(prefix_list[i] * suffix_list[i])

        return(result)