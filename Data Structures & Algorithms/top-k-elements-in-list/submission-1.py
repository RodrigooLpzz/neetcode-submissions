class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}

        for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1

        bucket = []
        for i in range(len(nums) + 1):
            bucket.append([])


        for key, value in dictionary.items():
            bucket[value].append(key)

        result = [] 
        for i in range(len(bucket) - 1, -1, -1):
            for j in range(len(bucket[i])):
                result.append(bucket[i][j])
                if len(result) == k:
                    return result
