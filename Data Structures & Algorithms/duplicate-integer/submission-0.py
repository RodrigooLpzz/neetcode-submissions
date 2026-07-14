class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap_nums = {}

        for i in nums:
            # hashmap_nums.get(i)
            if i in hashmap_nums:
                return True
            hashmap_nums[i] = 1
        
        return False