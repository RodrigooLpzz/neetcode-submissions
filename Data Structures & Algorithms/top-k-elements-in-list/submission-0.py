class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_nums = {}

        for num in nums:  # O(n)
            map_nums[num] = map_nums.get(num, 0) + 1 #O(1)

        bucket_sort = []
        for i in range(len(nums) + 1): # O(n)
            bucket_sort.append([]) # O(1)


        for key, value in map_nums.items(): # O(n)
            bucket_sort[value].append(key)  # O(1)

        # O(n) right now
        result = []

        for i in range(len(bucket_sort) - 1, -1, -1):
            for list_nums in bucket_sort[i]:
                result.append(list_nums)
                if len(result) == k:
                    return result
        # O(n)